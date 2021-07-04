FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server 

RUN useradd -m -d /home/ch2 -s /bin/bash ch2
RUN useradd -m -d /home/ch2-cracked -s /bin/bash ch2-cracked
RUN echo 'ch2:7e95f28caf75a4f5848ece440c2a0e8d' | chpasswd
RUN ln -s /dev/null /home/ch2/.bash_history

EXPOSE 22


ENTRYPOINT service ssh start && tail -f /dev/null && echo shellmates{Y0U_ArE_n07_sUppO$3D_T0_$ee_THIs_pS_RUined_MY_D4y}
