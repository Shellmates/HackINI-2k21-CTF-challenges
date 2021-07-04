#!/bin/bash

while :; do
    socat -dd -T60 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"python3 /challenge/sudoku.py",stderr
done
