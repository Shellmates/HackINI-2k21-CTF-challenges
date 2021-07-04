#!/bin/bash

while :; do
    socat -dd tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:"echo $FLAG"
done
