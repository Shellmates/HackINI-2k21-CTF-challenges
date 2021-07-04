#!/usr/bin/python3
from string import ascii_uppercase, digits
import random
import os
import re

charset = ascii_uppercase + digits

flag = f"shellmates{{{'-'.join(''.join(random.choice(charset) for _ in range(5)) for _ in range(6))}}}"
open("flag.txt", "w").write(flag + "\n")

flag = flag.encode()

lookup = [_ for _ in range(len(flag))]
key = list(os.urandom(len(flag)))
random.shuffle(lookup)

encrypted_flag = [key[i] ^ j for i, j in zip(lookup, flag)]

shellcode = list(open("shellcode", "rb").read())
shellcode += lookup + key + encrypted_flag

a, b = 0, 1
for i in range(len(shellcode)):
    shellcode[i] ^= a & 0xFF
    a, b = b, a + b

prog = open("crackini.c").readlines()
for i in range(len(prog)):
    if "char shellcode" in prog[i]:
        prog[i] = f"char shellcode[] = {{ {', '.join(map(str, shellcode))} }};\n"
        break

open("crackini.c", "w").write("".join(prog))

f = open("../solution/README.md").read()
old_flag = re.search("shellmates{[^}]+}", f).group(0)
open("../solution/README.md", "w").write(f.replace(old_flag, flag.decode()))

f = open("../challenge.yml").read()
open("../challenge.yml", "w").write(f.replace(old_flag, flag.decode()))
