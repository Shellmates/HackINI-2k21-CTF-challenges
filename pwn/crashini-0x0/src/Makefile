CC=gcc
CFLAGS=-static -no-pie -fno-stack-protector
SOURCE=crashini.c
OUTFILE=../challenge/crashini

all: $(SOURCE)
	$(CC) $(SOURCE) $(CFLAGS) -o $(OUTFILE)
clean: $(OUTFILE)
	rm -f $(OUTFILE)
