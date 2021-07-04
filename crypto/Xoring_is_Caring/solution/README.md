# Xoring is Caring

## Write-up

```python
""" fortunately we have the flag format , we can use this with the xor properties to find the flag """
from pwn import *

enc =  b'\x8a\x16\xc1:\xdd\x9f\x0b\x1e\xf1\x88\x9b^\xce%\x9c\x91X\x04\xa5\xc0\x8d\x16\xcd%\x91\x9b\x19J\xe0\x93\x855\xc6y\x8a\x98\'n\xe9\xd4\x97\x10\xf7~\xce\x8e,a\xb1\xd7\xc9J\xcb"\x80' 

for i in range(0,44,10):
    KEY = xor(b'shellmates',enc[i:i+10])
    plain_text = xor(enc,KEY)
    if b'shellmates{' in  plain_text:
       print(plain_text)
```

## Flag

`shellmates{Kn0wn_Pl4in_73xT_4774ck}`
