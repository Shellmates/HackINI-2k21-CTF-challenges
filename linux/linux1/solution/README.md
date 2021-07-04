# linux1

## Solution 

Since we have the password of the user and we can see that it belongs to sudo we check `sudo -l`
and we find that he can run `/usr/bin/base64` as uesr `ch1-cracked` who can read the flag.txt.
So all what we need to do is read the flag using base64 then decode it 

### script

```bash
sudo -u ch1-cracked /usr/bin/base64 flag.txt  |base64 -d
```
