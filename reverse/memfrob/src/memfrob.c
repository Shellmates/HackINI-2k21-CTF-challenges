#define _GNU_SOURCE
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define KEY_SIZE 20


void disable_buffering(void);

int main(int argc, char *argv[]) {
  char input[KEY_SIZE];
  char key[KEY_SIZE] = "my_super_secret_key";
  ssize_t count;

  disable_buffering();

  memset(input, '\0', KEY_SIZE);
  memfrob(key, strlen(key));

  printf("Enter the key : ");
  count = read(STDIN_FILENO, input, KEY_SIZE);
  if (count < 0) {
    perror("read error");
    return EXIT_FAILURE;
  }
  if (count > 0 && input[count-1] == '\n') {
    input[count-1] = '\0';
  }

  if(strncmp(input, key, KEY_SIZE)) {
    printf("Wrong key!\n");
    return EXIT_FAILURE;
  } else {
    printf("Correct key!\n");
    system("/bin/cat flag.txt");
  }

  return EXIT_SUCCESS;
}

void disable_buffering(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}
