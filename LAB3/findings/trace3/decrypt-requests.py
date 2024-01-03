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

input_dir = 'requests'
output_dir = 'requests-decrypted'

for filename in os.listdir(input_dir):
    with open(os.path.join(input_dir, filename), 'r') as input_file:
        encoded = input_file.readlines()
    
    for line_number, line in enumerate(encoded[4:], start=5):
            encoded = line.strip()
            
            decryptedfile = decrypt(encoded, password)
            
            output_path = os.path.join(output_dir, f"{filename}")
            
            with open(output_path, 'wb') as result:
                result.write(decryptedfile)
