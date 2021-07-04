#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define BUFF_SIZE 256
#define NAME_SIZE 128

void disable_buffering() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void) {
    char *name = malloc(NAME_SIZE);
    char buff[BUFF_SIZE];
    char *idx;
    int name_length;
    disable_buffering();
    memset(buff, 0, BUFF_SIZE);
    printf("Hello there! my name is: ");
    system("whoami");
    printf("What about you, what is your name? ");
    if (!(name_length = read(0, name, NAME_SIZE))) {
        perror("read error");
        exit(1);
    }
    if ((idx = strchr(name, '\n')) != NULL) {
        *idx = '\0';
        name_length = idx - name;
    }
    memcpy(buff, name, name_length);
    strcat(
        buff + name_length,
        ", what a beautiful name, nice to meet you! :)\nBut I gtg now, cya!\n"
    );
    printf(buff);
    free(name);
    return 0;
}
