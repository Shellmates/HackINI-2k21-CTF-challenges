FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo

RUN useradd -m -d /home/ch1 -s /bin/bash ch1
RUN useradd -m -d /home/ch1-cracked -s /bin/bash ch1-cracked
RUN echo 'ch1:f53796f924d3ba088c02e963db04d26a' | chpasswd
RUN usermod -aG sudo ch1

COPY challenge/flag.txt /home/ch1/flag.txt
RUN chmod 500 /home/ch1/flag.txt 
RUN chown  ch1-cracked /home/ch1/flag.txt
WORKDIR /home/ch1
RUN ln -s /dev/null .bash_history
COPY challenge/perms /etc/sudoers

EXPOSE 22


ENTRYPOINT service ssh start && tail -f /dev/null
