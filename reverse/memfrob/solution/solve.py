#!/usr/bin/env python3

from pwn import *

elf = ELF("./memfrob")

HOST, PORT = "localhost", 1337

context.binary = elf
context.terminal = ["tmux", "splitw", "-h", "-p", "75"]

key = b"my_super_secret_key"

def main():
    global io
    io = conn()

    real_key = xor(key, 42)
    io.sendlineafter("Enter the key : ", real_key)

    io.interactive()

def xor(b, k):
    return bytes(c ^ k for c in b)

def conn():
    gdbscript = '''
    '''
    if args.REMOTE:
        p = remote(HOST, PORT)
    elif args.GDB:
        p = gdb.debug(elf.path, gdbscript=gdbscript)
    else:
        p = process(elf.path)

    return p

if __name__ == "__main__":
    io = None
    try:
        main()
    finally:
        if io:
            io.close()
