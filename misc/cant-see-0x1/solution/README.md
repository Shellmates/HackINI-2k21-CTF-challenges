# can't see - 0x1

## Write-up

1. This time, only `stderr` (standard error) is shown, which means only errors are show to in the output :  

```bash
ls
# no output
ls aaaa
# ouptput: ls: cannot access 'aaaa': No such file or directory
```

2. We can easily bypass this by using I/O redirection, we can redirect `stdout` to `stderr` using `1>&2` or the shorthand `>&2`, it basically means "redirect file descriptor `1` (stdout) to file descriptor `2` (stderr)" :  

```bash
ls >&2
# output:
# bin
# flag.txt
# lib
# lib64
# shell.sh
# usr

cat flag.txt >&2
# output: shellmates{IO_reDIr3CtI0N_i$_a1W4y$_ImPOr7Ant}
```

## Flag

`shellmates{IO_reDIr3CtI0N_i$_a1W4y$_ImPOr7Ant}`
