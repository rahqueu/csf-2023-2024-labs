#!/bin/bash

# put 3 images named {a,b,c}.png in a /images directory


directory="chunks"
mkdir "$directory"

if [ ! -d "$directory" ]; then
    mkdir "$directory"
else 
    cd "$directory"
    rm *
    cd ..
fi

sudo apt-get install exiv2

python Image_Chunk_Split_v7.5.2.py

mkdir Output
mkdir Output/Chunks


cp images/a.png Output/Chunks/a.png
cp images/b.png Output/Chunks/b.png
cp images/c.png Output/Chunks/c.png

exiv2 -M "set Xmp.xmpRights.WebStatement $(cat chunks/chunk_1.txt)" Output/Chunks/a.png
exiv2 -M "set Xmp.xmpRights.WebStatement $(cat chunks/fake_chunk.txt)" Output/Chunks/b.png
exiv2 -M "set Xmp.xmpRights.WebStatement $(cat chunks/chunk_2.txt)" Output/Chunks/c.png

rmdir -r "$directory"










