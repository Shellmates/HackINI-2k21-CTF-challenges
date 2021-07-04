FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /chroot/usr/bin /chroot/bin /chroot/lib64 && \
    cp /bin/sh /bin/grep /bin/cat /bin/ls /bin/which /bin/sleep /bin/sed /chroot/bin/ && \
    cp /usr/bin/cut /usr/bin/wc /usr/bin/awk /usr/bin/tr /usr/bin/tail /usr/bin/head /usr/bin/find /usr/bin/base64 /chroot/usr/bin/ && \
    cp -r /lib /chroot/ && \
    cp -r /usr/lib /chroot/usr/ && \
    cp /lib64/ld-linux-x86-64.so.2 /chroot/lib64

RUN mkdir /chroot/dev && \
    mknod /chroot/dev/null c 1 3 && \
    chmod 666 /chroot/dev/null

RUN useradd ctf

COPY entrypoint.sh /

COPY flag.txt shell.sh /chroot/

RUN chmod +x /entrypoint.sh /chroot/shell.sh

EXPOSE 1337

ENTRYPOINT ["./entrypoint.sh"]
