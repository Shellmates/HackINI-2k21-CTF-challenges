CC=gcc
CFLAGS=-no-pie -fstack-protector
SOURCE=formatini.c
OUTFILE=../challenge/formatini

all: $(SOURCE)
	$(CC) $(SOURCE) $(CFLAGS) -o $(OUTFILE)
clean: $(OUTFILE)
	rm -f $(OUTFILE)
