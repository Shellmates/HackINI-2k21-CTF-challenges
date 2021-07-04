#!/bin/sh

USERSPEC="ctf"
CHROOT_DIR="/chroot"
EXEC="chroot --userspec=${USERSPEC} ${CHROOT_DIR} /shell.sh"
PORT=1337

socat tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr
