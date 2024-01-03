#!/bin/bash

# !!!!!!!!!!!! CREATE IN THIS DIRECTORY THE VIDEO YOU WANT TO CORRUPT NAMING IT "video.mp4" !!!!!!!!!!!

# Copy the first 8 bytes from video.mp4 to file.dat
dd if=video.mp4 of=file.dat bs=1 count=4 conv=notrunc


# Copy the rest of the bytes after 20 bytes from video.mp4
dd if=video.mp4 of=file.dat bs=1 skip=8 seek=4

mkdir -p Output
mv file.dat Output/
