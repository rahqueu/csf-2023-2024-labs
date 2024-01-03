import zlib
import os
import json
import sys

# Z_SYNC_FLUSH suffix
ZLIB_SUFFIX = b'\x00\x00\xff\xff'
# create a shared zlib inflation context to run chunks through
inflator = zlib.decompressobj()

# ...
def on_websocket_message(msg):
    # initialize a buffer to store chunks
    buffer = bytearray()
    # always push the message data to your cache
    buffer.extend(msg)

    # check if the last four bytes are equal to ZLIB_SUFFIX
    if len(msg) < 4 or msg[-4:] != ZLIB_SUFFIX:
        return

    # if the message *does* end with ZLIB_SUFFIX,
    # get the full message by decompressing the buffers
    # NOTE: the message is utf-8 encoded.
    msg = inflator.decompress(buffer)
    buffer = bytearray()

    # here you can treat `msg` as either JSON or ETF encoded,
    # depending on your `encoding` param
    print(json.loads(msg))
    
    # write the msg variable to a new file output.json
    #with open('output.json', 'a') as f:
    #    f.write(str(json.loads(msg)))
    
    return 1

# prompt the user for the files directory
files_dir = input("Enter the files directory: " )

# loop through all files in the directory
for filename in os.listdir(files_dir):
    # construct the full path to the file
    filepath = os.path.join(files_dir, filename)

    # read the contents of the file
    with open(filepath, 'rb') as f:
        #print(f'Reading file: {filepath}')
        file_contents = f.read()

    # call the on_websocket_message function with the file contents as input
    on_websocket_message(file_contents)
    
