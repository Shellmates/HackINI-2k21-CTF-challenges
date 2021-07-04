# Unrecoverable

## Write-up

```python
import random 
from string import ascii_lowercase,digits

enc = "ctn44vmunc{3ghgsy_uto_coo2_gc_2asyoxg1ec}"

random.seed(2**1337 - 1)

chars = ascii_lowercase + digits 

shuffled_chars=[i for i in chars]
random.shuffle(shuffled_chars)
shuffled_chars = ''.join(shuffled_chars)


flag = ''
for i in enc:
    if i.isalnum():
        flag += chars[shuffled_chars.index(i)]
    else:
        flag += i

print(flag)
```

## Flag

`shellmates{f1x1ng_th3_s33d_1s_d4ng3r10us}`
