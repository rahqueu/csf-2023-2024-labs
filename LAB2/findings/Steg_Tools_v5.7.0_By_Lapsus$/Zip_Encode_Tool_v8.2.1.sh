#!/bin/bash

sudo apt-get install lz4

# Create a temporary zip file containing the copied contents
#Enter your password here
password="pw1"
#enter the zipName file here
tempZip="zip1.zip"
#enter the encoded file name
zipName="file"
zip -j -P "$password" "$tempZip" zipDecoyFiles/* corrupted.pdf

lz4 -z "$tempZip" > "$zipName"
rm "$tempZip"
base64 "$zipName" > "$zipName.com"
rm "$zipName"
xxd -p "$zipName.com" > "file.docx"
rm "$zipName.com"

mv "file.docx" ./Output
