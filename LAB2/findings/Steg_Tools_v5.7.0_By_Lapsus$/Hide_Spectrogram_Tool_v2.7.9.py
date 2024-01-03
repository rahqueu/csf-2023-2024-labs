import wave
import sys
import numpy as np
from PIL import Image


# --------------- PARAMETERS -------------
MAX_FREQUENCY = 22000 # Hz
MIN_FREQUENCY = 20 # Hz

# 44100Hz if we use the audible frequencies
# 88200Hz if we use the inaudible frequencies
DOUBLE_SAMPLE_RATE = 88200  # Sample rate in Hz
SAMPLE_RATE = 44100
FINAL_AMPLITUDE = 1

audible_flag_types = {
    "-i" : {
        "max_frequency": 44000, 
        "min_frequency": 23000, 
        "sample_rate": DOUBLE_SAMPLE_RATE
        },
    "-a" : {
        "max_frequency": MAX_FREQUENCY, 
        "min_frequency": MIN_FREQUENCY, 
        "sample_rate": SAMPLE_RATE
        },
    "-h" : {
        "max_frequency": 33000, 
        "min_frequency": 9000, 
        "sample_rate": DOUBLE_SAMPLE_RATE
        },
}


# determines how wide each pixel is in the spectrogram. 
# a good rule is to compute NSamples / SAMPLE_RATE and see how much time (in seconds) will be granted for each pixel
NSAMPLES_PER_PIXEL = 15000
FREQUENCY_RESOLUTION = 200 # number of vertical lines to represent the message in the spectrogram

# WAV Parameters - DO NOT CHANGE
N_CHANNELS = 1;
SAMPLE_WIDTH_BYTES = 2     # 2 bytes = 16-bit
# -----------------------------------------

image_filename = ""
precomputed_frequencies = {}

def parse_input():
    global image_filename
    global MAX_FREQUENCY
    global MIN_FREQUENCY
    global SAMPLE_RATE

    arguments = sys.argv
    if len(arguments) == 2:
        image_filename = arguments[1:][0]
    elif len(arguments) == 3 and arguments[1:][1] in audible_flag_types:
        image_filename = arguments[1:][0]
        parameters_of_flag = audible_flag_types[arguments[1:][1]]
        MAX_FREQUENCY = parameters_of_flag['max_frequency']
        MIN_FREQUENCY = parameters_of_flag['min_frequency']
        SAMPLE_RATE = parameters_of_flag['sample_rate']

        print("NOTE:")
        print("To make the audio completely inaudible, you need to go through a filter pass and remove the sound of frequencies between 20Hz-20KHz with other software (such as FLStudio). Else, you will still notice some clicking sounds which are a result from the superposition of the 22KHz-44KHz frequencies.")
    else:
        print("Expected arguments: <image_secret_filename> <audible_flag>")
        print("     audible_flag (optional): ")
        print("              '-a' to hide the secret in the audible frequencies (20Hz-20Khz), making the noise audible. It's the default mode when the flag is not provided.")
        print("              '-h' to hide half the secret in the audible frequencies (20Hz-20Khz), and the other half in inaudible frequencies (23Khz-44Khz).")
        print("              '-i' to hide the secret in the inaudible frequencies (22Hz-44Khz), making the noise barely audible")
        exit()



def precompute_frequency_samples(image_height):
    """
    Precomputes the defined number of samples by the variable NSAMPLES_PER_PIXEL 
    for each frequency line used.
    The number of frequency lines depends on the FREQUENCY_RESOLUTION
    Used to speedup the program - when summing up the frequencies corresponding to the pixels of the image
    we use the precomputed array of NSAMPLES_PER_PIXEL which corresponds to a sine wave with the frequency corresponding
    to the pixel's height index
    """
    freq_range_per_pixel = int((MAX_FREQUENCY - MIN_FREQUENCY) / image_height)
    freq_line_delta = (MAX_FREQUENCY - MIN_FREQUENCY) / FREQUENCY_RESOLUTION
    frequency_range_top = MAX_FREQUENCY # height index starts from top of the image, thus we start from highest frequency
    frequency_line = frequency_range_top
    frequency_range_bottom = frequency_range_top - freq_range_per_pixel + 1

    time_per_pixel = NSAMPLES_PER_PIXEL / SAMPLE_RATE
    t_pixel =  np.linspace(0, time_per_pixel, int(NSAMPLES_PER_PIXEL), False) # time passage

    for height in range(image_height):
        # for each frequency line on the current height pixel range, add the computed frequency samples to the precomputed map
        while frequency_line > MIN_FREQUENCY and frequency_range_bottom  <= frequency_line <= frequency_range_top:
            precomputed_frequency = np.zeros(NSAMPLES_PER_PIXEL)
            for s in range(NSAMPLES_PER_PIXEL):
                precomputed_frequency[s] = np.sin(2 * np.pi * frequency_line * t_pixel[s])
            precomputed_frequencies[frequency_line] = precomputed_frequency
            frequency_line -= freq_line_delta
        frequency_range_top -= freq_range_per_pixel
        frequency_range_bottom = frequency_range_top - freq_range_per_pixel + 1



def create_wav_file(sample_array, min_possible_val, max_possible_val):
    """
    Normalizes the image array, and writes it to a .wav file without compression
    """
    # Ensure that highest value is in 16-bit range
    sample_width_int = (2**(SAMPLE_WIDTH_BYTES*8)) / 2 - 1
    # normalize the signal to a range in [-sample_width_int, sample_width_int]
    minus_one_one_normalized = 2 * ( (sample_array - min_possible_val)  / (max_possible_val - min_possible_val) ) - 1
    audio = np.int16(minus_one_one_normalized *  FINAL_AMPLITUDE * sample_width_int)
    # print("nomalied signal:", audio)

    with wave.open('./Output/my-fav-song.wav', 'w') as wav_file:
        # Set the parameters
        wav_file.setparams((N_CHANNELS, SAMPLE_WIDTH_BYTES, SAMPLE_RATE, 0, 'NONE', 'not compressed'))
        
        # Write the audio
        wav_file.writeframes(audio.tobytes())


def convert_image_to_audio(image_array):
    """
    Converts image pixels into frequency lines.
    Uses the precomputed frequency lines vector


    image_array: 2D array representing the pixels in grayscale, with values ranging from 0 to 1.
    """
    image_width = image_array.shape[1]
    image_height = image_array.shape[0]
    freq_range_per_pixel = int((MAX_FREQUENCY - MIN_FREQUENCY) / image_height)
    freq_line_delta = (MAX_FREQUENCY - MIN_FREQUENCY) / FREQUENCY_RESOLUTION
    
    signal = np.zeros(image_width * NSAMPLES_PER_PIXEL)

    for width in range(image_width):
        frequency_range_top = MAX_FREQUENCY # height index starts from top of the image, thus we start from highest frequency
        frequency_line = frequency_range_top
        frequency_range_bottom = frequency_range_top - freq_range_per_pixel + 1
        for height in range(image_height):

            # sum sample values of all pixels of same column and create NSAMPLES_FOR_EACH_PIXEL number of samples
            while frequency_line > MIN_FREQUENCY and frequency_range_bottom  <= frequency_line <= frequency_range_top:
                if image_array[height, width] != 0: # if pixel has value, create the samples for that
                    index = width*NSAMPLES_PER_PIXEL
                    signal[index: index + NSAMPLES_PER_PIXEL] += image_array[height, width] * precomputed_frequencies[frequency_line]
                frequency_line -= freq_line_delta
            frequency_range_top -= freq_range_per_pixel
            frequency_range_bottom = frequency_range_top - freq_range_per_pixel + 1

        if frequency_range_top < MIN_FREQUENCY: 
            continue

    return signal

# --------- MAIN ---------

parse_input()

print("Starting encoding the secret...")
# open & cinvert image to greyscale
img = Image.open(image_filename)
img_gray = img.convert("L")
img_array = np.array(img_gray)
# normalize to [0,1] values
img_normalized = 1 - (img_array / 255.0)

precompute_frequency_samples(img_normalized.shape[0])
signal = convert_image_to_audio(img_normalized)
create_wav_file(signal, -FREQUENCY_RESOLUTION, FREQUENCY_RESOLUTION)

print("Done. Your secret is hidden in the audio file 'my-fav-song.wav' and is only visible using a spectrogram.")
print("Now to hide it better, join it with another audio (with the help of any other software)")
