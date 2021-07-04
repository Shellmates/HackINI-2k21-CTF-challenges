#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

void disable_buffering(void);
void www(void);

int main(int argc, char *argv[]) {
  char name[32];

  disable_buffering();

  printf("Welcome!\n");
  printf("You might need this: %p\n", printf);

  printf("Enter your name: ");
  read(0, name, 32);

  www();

  puts(name);

  return EXIT_SUCCESS;
}

void disable_buffering(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void www(void) {
  char buf[16];
  unsigned long *address;
  unsigned long value;

  printf("You have only one shot, choose wisely!\n");

  printf("Where? ");
  read(0, buf, 16);
  address = (unsigned long*)strtoull(buf, NULL, 10);

  printf("What? ");
  read(0, buf, 16);
  value = strtoull(buf, NULL, 10);

  *address = value;
}
