# just /bin/bash

## Write-up

1. Just like the description indicates, only `/bin/bash` is installed so we cannot use usual commands like `ls` and `cat`.

2. The idea is to use the built-in commands provided by `bash` to list the files in current directory and read the flag.

3. List files in current directory using `echo` built-in command with bash glob expansion :  

```bash
echo *
# output: bin flag.txt lib lib64
```

4. Read flag file using `read` built-in command and input redirection :  

```bash
read flag <flag.txt
echo $flag
# output: shellmates{sH3ll_built1ns_FTW}
```

## Flag

`shellmates{sH3ll_built1ns_FTW}`
