FROM python:3.8

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

COPY challenge /challenge

RUN chmod 500 /challenge/run.sh

EXPOSE 1337

ENTRYPOINT ["/challenge/run.sh"]
