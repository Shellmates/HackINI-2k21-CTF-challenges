FROM ubuntu

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

RUN useradd ctf

COPY run.sh /
RUN chmod +x /run.sh

EXPOSE 1337

ENTRYPOINT ["/run.sh"]
