# www

## Write-up

- Source code :  

```c
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
```

- `www` stands for Write What Where, which is a class of vulnerabilities where you can write any value to any address in memory
- In this challenge, we're first greeted with a libc leak (printf@libc), which is going to be useful later for our WWW attack
- In the `www` function, we're allowed to write 8 bytes to any address
- Let's check if GOT table is writable (using `checksec ./www`) :  

```txt
[*] '/home/malik/shellmates/hackini-2k21/HackINI-2k21-CTF/pwn/www/solution/www'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

- RELRO is partial which means the GOT table is writable
- That means we can change an entry in the GOT table such that a libc function in the GOT points to any other function
- Since we already have a libc leak we can overwrite the GOT entry of `puts` with `system@libc`, especially since `puts` is called after the `www` function and has `name` as its first argument, which is a controllable input from the earlier `read`
- Basically we're doing : `puts@GOT = system@libc`

- Full automated exploit with pwntools [here](solve.py)

## Flag

`shellmates{WrITE_Wh44AA4AT_WH3r3}`
