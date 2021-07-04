# Hide and Hide

## Write-up

1. This is a steganography challenge, which means some data (text) is hidden in a document (image)

2. Given that the flag format is `shellmates{}`, we can start by looking for "shellmates" string in [logo.png]("../logo.png") :  

```bash
string logo.png | grep shellmates
# output: shellmates{57394n0924_phy_I5_1E37}
```

## Flag

`shellmates{57394n0924_phy_I5_1E37}`
