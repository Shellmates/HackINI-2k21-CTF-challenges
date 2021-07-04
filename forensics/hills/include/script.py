#!/usr/bin/python3.8

# Code inspired from https://github.com/arunKumar/Hide-in-png
# Hiding File in PNG

import struct
import sys
import binascii
import base64

args = sys.argv

if(len(sys.argv)<1): 
    print('Usage: %s <input.png>' % (args[0]))
    sys.exit(0)

png = open(args[1], 'rb').read()

custom_header = b'shellmates{nOt_4_flaG}'
flag = open('zip.gz','rb').read()
flag = custom_header + base64.b64encode(flag)
# The flag is in a zip file encoded in base64
i = 8 

f = open('green-hills.png', 'wb')

# Writing png signiture
f.write(png[:i])

while (i<len(png)):
    previous_len = i
    chunk_len,chunk_type = struct.unpack('>I4s', png[i:i+8])
    i += 8 + chunk_len + 4

    if (chunk_type == b'IHDR'):
        chunk_length = struct.pack('>I',len(flag))
        chunk_header = struct.pack('%ds'%(len(b'FLAG')), b'FLAG')
        chunk_crc = binascii.crc32(chunk_header+flag) & 0xffffffff
        chunk_crc_hex = struct.pack('>I',chunk_crc)
        f.write(chunk_length + chunk_header + flag + chunk_crc_hex)

    f.write(png[previous_len:i])
