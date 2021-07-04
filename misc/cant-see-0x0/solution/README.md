# can't see - 0x0

## Write-up

1. Upon connecting to the challenge server, we're effectively greeted with a `/bin/bash` shell

2. List files in current directory :  

```bash
ls
# output:
# bin
# flag.txt
# lib
# lib64
# shell.sh
# usr
```

3. Read flag file :  

```bash
cat flag.txt
# output: shellmates{GOo0Od_wARmuP_F0r_Wh47$_n3xT}
```

## Flag

`shellmates{GOo0Od_wARmuP_F0r_Wh47$_n3xT}`
