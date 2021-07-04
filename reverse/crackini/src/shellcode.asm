bits 64

%idefine flag_size 47
%idefine shellcode_size 85

section .text
code:
    lea rsi, [rel $]
    xor rcx, rcx
    jmp strlen
inc_rcx:
    inc rcx
strlen:
    mov al, [rdi + rcx]
    test al, al
    jne inc_rcx
    cmp rcx, flag_size
    jne bad
    xor rdx, rdx
    xor rax, rax
verify:
    mov al, [rsi + rdx + shellcode_size]
    mov al, [rsi + rax + shellcode_size + flag_size]
    mov bl, [rdi + rdx]
    xor al, bl
    mov bl, [rsi + rdx + shellcode_size + flag_size*2]
    cmp al, bl
    jne bad
    dec rcx
    inc rdx
    test rcx, rcx
    jne verify
    xor rax, rax
    jmp return
bad:
    mov rax, 1
    jmp return
return:
    ret
