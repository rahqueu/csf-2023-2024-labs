from urllib.parse import unquote
import os
import base64
from Crypto.Cipher import AES
import hashlib

password = "CZN.pjp0paz3jej5jgajcj!hzx3yzp2DTB1hgy"

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = unquote(enc)
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return cipher.decrypt(enc[16:])

input_dir = 'to-decrypt'
output_dir = 'decrypted'

for filename in os.listdir(input_dir):
    if filename.endswith('.aspx'):
        if(filename != "missing-file.aspx"):
            continue

        with open(os.path.join(input_dir, filename), 'r') as input_file:
            encoded = input_file.read()
        
        if encoded.startswith("file="):
            encoded = encoded[len("file="):]
        elif encoded.startswith("cmd="):
            encoded = encoded[len("cmd="):]
        
        decryptedfile = decrypt(encoded, password)
        
        output_filename, _ = os.path.splitext(filename)
        
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, 'wb') as result:
            result.write(decryptedfile)
