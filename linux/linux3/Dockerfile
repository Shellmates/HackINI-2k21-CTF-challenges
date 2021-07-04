FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo

RUN useradd -m -d /home/ch3 -s /bin/bash ch3
RUN useradd -m -d /home/ch3-cracked -s /bin/bash ch3-cracked
RUN echo 'ch3:dfae0b45a58cfd9d903d872861389b20' | chpasswd
RUN usermod -aG sudo ch3

COPY challenge/flag.txt /home/ch3/flag.txt
RUN chmod 550 /home/ch3/flag.txt 
RUN chown  ch3-cracked /home/ch3/flag.txt
RUN ln -s /dev/null /home/ch3/.bash_history
WORKDIR /home/ch3
COPY challenge/perms /etc/sudoers
COPY challenge/read.py /home/ch3/read.py
run chmod 755 /home/ch3/read.py

EXPOSE 22


ENTRYPOINT service ssh start && tail -f /dev/null
