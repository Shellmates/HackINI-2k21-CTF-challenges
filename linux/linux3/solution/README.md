# linux3

## Solution 

We can notice that we can read the file `/home/ch3/not_the_flag` using the root permission when checking `sudo -l` .In order to be able 
to read the flag we must find a way to that file point to the the flag and symlink is the way to do that so it will become like this 
`/home/ch3/not_the_flag --> /home/ch3/flag.txt`

### script

```bash
ln -s /home/ch3/flag.txt /home/ch3/not_the_flag && sudo -u root /home/ch3/read.py
```
