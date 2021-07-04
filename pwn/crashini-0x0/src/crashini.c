#include <stdio.h>
#include <signal.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

#define INTRO "Hello world!\n" \
              "This is my first C program :)\n" \
              "Our teacher gave us an assignement and told us to use gets if we wanted " \
              "to read user input, which I did!\n" \
              "But I don't understand why the compiler is telling me not to use it :(, I'm " \
              "getting: \"warning: the `gets' function is dangerous and should not be used.\"\n" \
              "I searched stackoverflow, and saw people talking about some buffer overflow thingy, " \
              "what does that even mean?\n" \
              "I also checked the man page for gets using `man gets` and it says " \
              "`Never use this function`. wth?\n" \
              "Tell me why plzz: "
char *shell = "/bin/sh";

void sigsegv_handler() {
    int n, fd = open("flag1.txt", O_RDONLY);
    char flag[128];
    for (n = 0; n < sizeof(flag) && read(fd, flag + n, 1); n++);
    write(1, flag, n);
    exit(1);
}

void daddy_i_learned_to_hijack_the_program_s_control_flow() {
    int n, fd = open("flag2.txt", O_RDONLY);
    char flag[128];
    for (n = 0; n < sizeof(flag) && read(fd, flag + n, 1); n++);
    write(1, flag, n);
    exit(2);
}

void disable_buffering() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void) {
    char buff[128];
    disable_buffering();
    signal(SIGSEGV, sigsegv_handler);
    printf(INTRO);
    gets(buff);
    puts("I still don't understand, but it's fine :<");
    return 0;
}
