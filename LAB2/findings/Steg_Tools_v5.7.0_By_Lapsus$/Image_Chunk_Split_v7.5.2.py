import base64
import sys
import os
import random
import string
from base64io import Base64IO as b64


def split_image_to_chunks(input_image_file, output_directory, chunk_size):
    try:
        counter = 1000  # Corrected indentation
        with open(input_image_file, "rb") as image_file:
            image_data = image_file.read()

        # Rest of the code...
        num_chunks = len(image_data) // chunk_size + 1

        for i in range(num_chunks):
            chunk_start = i * chunk_size
            chunk_end = (i + 1) * chunk_size
            chunk_data = image_data[chunk_start:chunk_end]

            encoded_data = base64.b64encode(chunk_data).decode("utf-8")
            output_file = f"{output_directory}/chunk_{i + 1}.txt"

            with open(output_file, "w") as chunk_file:
                chunk_file.write(encoded_data)
        aux = open(f"{output_directory}/fake_chunk.txt", mode='wb')
        fakeChunk = b64(aux)
        while counter != 0:
            #add random byte sequences to the before and after the decoy string"
            random_prefix = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(13)
            )
            random_suffix = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(11)
            )
            chunk_datas = "YOUWISH_AHAHA"
            chunk_data = f"{random_prefix}{chunk_datas}{random_suffix}"
            encoded_data = fakeChunk.write(chunk_data.encode("utf-8"))
            counter -= 1
            print(
                #f"Successfully split {input_image_file} into {num_chunks} Base64-encoded chunks."
            )
        fakeChunk.close()
        aux.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    input_image_file = "images/tunnelBlueprint.jpeg"  # Replace with your input image file
    chunk_size = (
        round(os.path.getsize(input_image_file) / 2) + 100
    )  # Chunk size in bytes plus an extra 100 bytes
    output_directory = "chunks"  # Directory where Base64-encoded chunks will be saved
    split_image_to_chunks(input_image_file, output_directory, chunk_size)
