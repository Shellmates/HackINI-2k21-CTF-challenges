FROM ubuntu

RUN apt-get update && \
    apt-get install -y openssh-server

RUN mkdir -p /chroot/lib/x86_64-linux-gnu /chroot/lib64 /chroot/bin && \
    cp /lib/x86_64-linux-gnu/libc.so.6 /chroot/lib/x86_64-linux-gnu && \
    cp /lib/x86_64-linux-gnu/libtinfo.so.6 /chroot/lib/x86_64-linux-gnu && \
    cp /lib/x86_64-linux-gnu/libdl.so.2 /chroot/lib/x86_64-linux-gnu && \
    cp /lib64/ld-linux-x86-64.so.2 /chroot/lib64 && \
    cp /bin/bash /chroot/bin

RUN useradd -ms /bin/bash ctf && \
    echo 'ctf:ctf' | chpasswd

COPY sshd_config /etc/ssh/

COPY flag.txt /chroot

EXPOSE 22

ENTRYPOINT service ssh start && tail -f /dev/null
