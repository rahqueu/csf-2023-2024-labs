from PIL import Image
import numpy as np
import sys


def lsb_decoder(n, image_path, output_file):
    """ 
    Extracts the n LSBs from 'image_path' and saves them in 'output_file'.
    This function was made specifically for the 'logo.png' image, as it 
    extracts the LSB(n) from every pixel except for the blue ones.
    """
    # Gets all the LSBs from LSB(1) to LSB(n)
    try:
        img = Image.open(image_path, 'r')
        img_data = np.array(list(img.getdata()))

        num_pixels = img_data.size//3

        for i in range(1, int(n)+1):

            extracted_bits = ""
            num_extracted = 0
            for x in range(num_pixels):
                    pixel = tuple(img_data[x][:3])

                    if pixel != (0, 159, 227): # Blue color we want to avoid.

                        for p in range(0, 3):
                            # Extracts the last i bits from the pixel
                            extracted_bits += ((bin(pixel[p])[2:]).zfill(8))[-i:]
                            num_extracted += i

            extracted_bits = [extracted_bits[b:b+8] for b in range(0, len(extracted_bits), 8)]

            secret = bytearray()
            for e in range(len(extracted_bits)):
                secret.append(int(extracted_bits[e], 2))

                if num_extracted >= len(extracted_bits)*8:
                    break;

            open(f"{output_file}_lsb{i}", 'wb').write(secret)

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: lsb_decoder.py <n> <image> <output_file>")

    else:
        n = sys.argv[1]
        image = sys.argv[2]
        output_file = sys.argv[3]
        lsb_decoder(n, image, output_file)