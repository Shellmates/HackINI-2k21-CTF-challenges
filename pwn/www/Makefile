CC=gcc
CFLAGS=-no-pie
SOURCE=src/www.c
OUTFILE=challenge/www

build: $(SOURCE)
	$(CC) $(CFLAGS) -D BuiltWithMake -o $(OUTFILE) $(SOURCE)
	chmod +x $(OUTFILE)
