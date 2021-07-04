import random 
from string import ascii_lowercase,digits
from secret import flag

chars = ascii_lowercase + digits 

random.seed(2**1337 - 1)

shuffled_chars=[i for i in chars]
random.shuffle(shuffled_chars)
shuffled_chars = ''.join(shuffled_chars)
#print(f"{chars}\n{''.join(shuffled_chars)}");input()

enc = ''
for i in flag:
    if i.isalnum():
        enc += shuffled_chars[chars.index(i)]
    else:
        enc+=i

print(enc)
#  ctn44vmunc{3ghgsy_uto_coo2_gc_2asyoxg1ec}