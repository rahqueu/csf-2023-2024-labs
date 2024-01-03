#!/bin/bash

# CREATE A DIRECTORY WITH ALL THE IMAGES AND AUDIO NAMED "video"
# NAME THE IMAGES FROM 1 TO 15
# First argument is the secret file path

sudo apt-get install ffmpeg
sudo apt-get install imagemagick # convert command

pip install bitstring

# direcotry with all the images and audio for the video
direc=video
# secret filepath
secretPath=$1

cd "./$direc"

convert image14.png -resize 800x800! secretFrame.png

cd ..
python LSB_Video_Tool_v7.8.1.py h "./$direc/secretFrame.png" "$secretPath" g

cd "./$direc"
ffmpeg -loop 1 -t 4 -i image1.png -loop 1 -t 4 -i image2.png -loop 1 -t 4 -i image3.png -loop 1 -t 4 -i image4.png -loop 1 -t 4 -i image5.png -loop 1 -t 4 -i image6.png -loop 1 -t 4 -i image7.png -loop 1 -t 4 -i image8.png -loop 1 -t 4 -i image9.png -loop 1 -t 4 -i image10.png -loop 1 -t 4 -i image11.png -loop 1 -t 4 -i image12.png -loop 1 -t 4 -i image13.png -loop 1 -t 4 -i image15.png -loop 1 -t 4 -i secretFrame.png -filter_complex "[0:v]fps=1,scale=800:800[v0];[1:v]fps=1,scale=800:800[v1];[2:v]fps=1,scale=800:800[v2];[3:v]fps=1,scale=800:800[v3];[4:v]fps=1,scale=800:800[v4];[5:v]fps=1,scale=800:800[v5];[6:v]fps=1,scale=800:800[v6];[7:v]fps=1,scale=800:800[v7];[8:v]fps=1,scale=800:800[v8];[9:v]fps=1,scale=800:800[v9];[10:v]fps=1,scale=800:800[v10];[11:v]fps=1,scale=800:800[v11];[12:v]fps=1,scale=800:800[v12];[13:v]fps=1,scale=800:800[v13];[14:v]fps=1,scale=800:800[v14];[v0]setsar=sar=1[v0];[v1]setsar=sar=1[v1];[v2]setsar=sar=1[v2];[v3]setsar=sar=1[v3];[v4]setsar=sar=1[v4];[v5]setsar=sar=1[v5];[v6]setsar=sar=1[v6];[v7]setsar=sar=1[v7];[v8]setsar=sar=1[v8];[v9]setsar=sar=1[v9];[v10]setsar=sar=1[v10];[v11]setsar=sar=1[v11];[v12]setsar=sar=1[v12];[v13]setsar=sar=1[v13];[v14]setsar=sar=1[v14];[v0][v1][v2][v3][v4][v5][v6][v7][v8][v9][v10][v11][v12][v13][v14]concat=n=15:v=1:a=0[v]" -i audio.mp3 -map "[v]" -map 15:a -c:v libx264rgb -crf 0 -shortest ../Output/video.mp4

rm work.png


