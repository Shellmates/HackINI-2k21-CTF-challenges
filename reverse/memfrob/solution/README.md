# memfrob

## Write-up

- Source code :  

```c
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
```

- `memfrob(void *s, size_t n)` is a function that "frobnicates" a memory area : it encrypts the first `n` bytes of the memory area `s` by XORing each character with the number 42
- Goal is to XOR the key `"my_super_secret_key"` with 42, and send the result as input
- We can get that result with the following Python code :  

```python
def xor(b, k):
    return bytes(c ^ k for c in b)

key = b"my_super_secret_key"
real_key = xor(key, 42)
print(real_key)
```

- Full automated exploit with pwntools [here](solve.py)

## Flag

`shellmates{mEmFRob_i$_JusT_$1mplE_xOoOor}`
