# WildShark

## Write-up

1. Open the capture.pcapng file using Wireshark
2. Explore packets until arriving at Packet No. 19
3. Go to Analyze > Follow Stream > TCP Stream
4. You notice the following conversation :
```txt
hello
hey wssup bro
good wbu
doin good bro
listen on 1337
I'll send you the flag
ok
```
5. Use Filter: tcp.port == 1337
6. Go to Analyze > Follow Stream > TCP Stream
in the new window select show data as RAW and export the file
7. file the exported file shows that this is an ELF.
8. strings the exported file you'll get the following :
```txt
...
/lib64/ld-linux-x86-64.so.2
libc.so.6
__stack_chk_fail
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
GLIBC_2.4
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
shellmatH
es{$treaH
ms_4re_cH
0o1}
[]A\A]A^A_
:*3$"
GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8060
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
ccc.c
__FRAME_END__
__init_array_end
_DYNAMIC
...
```
we notice :
```txt
shellmatH
es{$treaH
ms_4re_cH
0o1}
```
the flag is : 
`shellmates{$treams_4re_c0o1}`

## Flag
`shellmates{$treams_4re_c0o1}`
