from PIL import Image
from bitstring import BitArray
import sys

NLSB = 4
END_SIGN = b"END"

def readable_size(value: int) -> str:
	if value < 1024:
		return f'{value}B'
	elif value < 1024**2:
		return f'{value/1024:.2f}KB'
	elif value < 1024**3:
		return f'{value/1024**2:.2f}MB'
	else:
		return f'{value/1024**3:.2f}GB'

def print_progress_bar(current: int, total: int):
	max_size = 80
	bar_size = round(max_size * current / total)
	print(f'[{"■"*bar_size}{"-"*(max_size-bar_size)}] ({readable_size(current)}/{readable_size(total)}){" "*10}', end='\r', flush=True)

def get_new_color_value(red: int, payload_bits: BitArray) -> int:
	new_red = BitArray(red.to_bytes(1, 'big'))
	new_red.overwrite(payload_bits, 8-NLSB)
	return new_red.uint


def hide(path_to_original: str, path_to_payload: str, color_idx: int):
	original = Image.open(path_to_original)
	with open(path_to_payload, mode='rb') as file:
		payload_bits = BitArray(file.read() + END_SIGN)

	max_payload_size = original.width * original.height * NLSB

	if payload_bits.length > max_payload_size:
		exit(f"Impossible to hide payload ({readable_size(payload_bits.length//8)}) in given file with NLSB={NLSB}, maximum is {readable_size(max_payload_size//8)}")

	i = 0
	for y in range(original.height):
		for x in range(original.width):
			original_rgb = original.getpixel((x, y))
			new_color_value = get_new_color_value(original_rgb[color_idx], payload_bits[i:i+NLSB])
			print_progress_bar(i // 8, payload_bits.length // 8)
			if color_idx == 0:
				original.putpixel((x, y) , (new_color_value, original_rgb[1], original_rgb[2]))
			elif color_idx == 1:
				original.putpixel((x, y) , (original_rgb[0], new_color_value, original_rgb[2]))
			else:
				original.putpixel((x, y) , (original_rgb[0], original_rgb[1], new_color_value))
			i += NLSB
			if i >= len(payload_bits):
				original.save(path_to_original)
				original.close()
from PIL import Image
from bitstring import BitArray
import sys

NLSB = 6
END_SIGN = b"END"

def readable_size(value: int) -> str:
	if value < 1024:
		return f'{value}B'
	elif value < 1024**2:
		return f'{value/1024:.2f}KB'
	elif value < 1024**3:
		return f'{value/1024**2:.2f}MB'
	else:
		return f'{value/1024**3:.2f}GB'

def print_progress_bar(current: int, total: int):
	max_size = 80
	bar_size = round(max_size * current / total)
	print(f'[{"■"*bar_size}{"-"*(max_size-bar_size)}] ({readable_size(current)}/{readable_size(total)}){" "*10}', end='\r', flush=True)

def get_new_color_value(red: int, payload_bits: BitArray) -> int:
	new_red = BitArray(red.to_bytes(1, 'big'))
	new_red.overwrite(payload_bits, 8-NLSB)
	return new_red.uint


def hide(path_to_original: str, path_to_payload: str, color_idx: int):
	original = Image.open(path_to_original)
	with open(path_to_payload, mode='rb') as file:
		payload_bits = BitArray(file.read() + END_SIGN)

	max_payload_size = original.width * original.height * NLSB

	if payload_bits.length > max_payload_size:
		exit(f"Impossible to hide payload ({readable_size(payload_bits.length//8)}) in given file with NLSB={NLSB}, maximum is {readable_size(max_payload_size//8)}")

	i = 0
	for y in range(original.height):
		for x in range(original.width):
			original_rgb = original.getpixel((x, y))
			new_color_value = get_new_color_value(original_rgb[color_idx], payload_bits[i:i+NLSB])
			print_progress_bar(i // 8, payload_bits.length // 8)
			if color_idx == 0:
				original.putpixel((x, y) , (new_color_value, original_rgb[1], original_rgb[2]))
			elif color_idx == 1:
				original.putpixel((x, y) , (original_rgb[0], new_color_value, original_rgb[2]))
			else:
				original.putpixel((x, y) , (original_rgb[0], original_rgb[1], new_color_value))
			i += NLSB
			if i >= len(payload_bits):
				original.save(path_to_original)
				original.close()
				return

def extract_payload_bits(color_value: int) -> BitArray:
	red_bits = BitArray(color_value.to_bytes(1, 'big'))
	return red_bits[8-NLSB:]

def solve(path_to_stego: str, color_idx: int, file_ext: str):
	original = Image.open(path_to_stego)
	payload_bits = BitArray()

	total_bytes = original.height * original.width * NLSB // 8

	for y in range(original.height):
		for x in range(original.width):
			red = original.getpixel((x, y))[color_idx]
			payload_bits.append(extract_payload_bits(red))
			print_progress_bar(payload_bits.length // 8, total_bytes)
	with open("../secrets/secret_recovered", mode='wb') as file:
		extra_bits = payload_bits.length % 8
		if (extra_bits != 0):
			payload_bits = payload_bits[:payload_bits.length - extra_bits]
		
		if (file_ext == "png"):
			endidx = payload_bits.bytes.find(b"\x49\x45\x4E\x44") + 8
		elif (file_ext in ["jpg", "jpeg"]):
			endidx = payload_bits.bytes.find(b"\xFF\xD9") + 2
		else:
			endidx = len(payload_bits.bytes)
		file.write(payload_bits.bytes[:endidx])

def rgb_str_to_n(char: str):
	if char == 'r':
		return 0
	elif char == 'g':
		return 1
	elif char == 'b':
		return 2
	else:
		exit("Invalid color")

if __name__ == "__main__":
	if len(sys.argv) >= 4 and sys.argv[1] in ["h", "s"]:
		if sys.argv[1].lower() == "h":
			hide(sys.argv[2], sys.argv[3], rgb_str_to_n(sys.argv[4]))
		elif sys.argv[1].lower() == "s":
			solve(sys.argv[2], rgb_str_to_n(sys.argv[3]), sys.argv[4].lower())
		else:
			exit("Usage: python lsb.py h <path to original> <path to payload> <color char>\nOr: python lsb.py s <path to stego> <color char> <file extension>")
	else:
		exit("Usage: python lsb.py h <path to original> <path to payload> <color char>\nOr: python lsb.py s <path to stego> <color char> <file extension>")

