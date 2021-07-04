# RSA1

## Write-up

```python
from Crypto.Util.number import long_to_bytes,inverse
""" n is relatively small , so we cant factorize it easily """ 
enc  = 713822463491939628949080236459794906441914407944768290378695739068636927695199214947719158013040

 
p = 9942874965373398689
q = 102411157768469768587484356311902427789461430190314198242306101223897141593967

N = p * q
e = 65537
phi = (p-1) * (q-1)
d = inverse(e,phi)

flag = long_to_bytes(pow(enc,d,N)).decode()
print(flag)
```

## Flag

`shellmates{U_5h0uld_U53_L4rg3_Numb3r5}`
