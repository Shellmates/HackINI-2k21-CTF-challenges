bits 64

global fun1
global fun2
global fun3

section .data

ZG5k3r9:
db 36, 221, 193, 137, 10, 207, 131, 226, 198, 253, 127, 70, 68, 37, 157, 46, 39, 32, 184, 225, 53, 57, 51, 177, 144, 200, 48, 169, 152, 117, 115, 234, 248, 54, 64, 35, 164, 41, 105, 93, 21, 145, 196, 11, 228, 172, 55, 149, 60, 99, 82, 133, 224, 30, 243, 255, 130, 132, 181, 187, 151, 146, 150, 18, 142, 74, 214, 73, 122, 155, 139, 52, 12, 143, 213, 239, 44, 90, 58, 202, 197, 110, 160, 103, 13, 140, 31, 245, 7, 29, 91, 79, 159, 171, 5, 166, 129, 83, 63, 251, 246, 236, 15, 78, 66, 156, 8, 107, 186, 242, 75, 95, 25, 20, 84, 194, 76, 28, 92, 113, 254, 162, 161, 27, 3, 216, 100, 17, 38, 109, 14, 24, 203, 112, 235, 81, 98, 104, 45, 67, 89, 1, 0, 119, 88, 170, 189, 230, 49, 238, 135, 223, 26, 47, 85, 182, 240, 106, 80, 50, 101, 6, 180, 118, 217, 34, 108, 190, 232, 165, 154, 111, 72, 87, 201, 4, 249, 205, 212, 219, 33, 233, 43, 174, 222, 124, 123, 69, 244, 192, 9, 121, 147, 250, 229, 77, 163, 206, 191, 179, 125, 86, 59, 148, 176, 134, 97, 158, 227, 252, 208, 138, 42, 102, 128, 183, 218, 247, 22, 199, 56, 167, 195, 211, 209, 94, 71, 141, 168, 16, 65, 220, 96, 136, 120, 61, 237, 188, 62, 241, 173, 175, 114, 23, 2, 126, 215, 185, 153, 40, 116, 204, 178, 231, 210, 19

fun_table:
dq push_rbx
dq fakejmp
dq set_rbx
dq fakejmp
dq fakejmp
dq xlatb_instr
dq fakejmp
dq pop_rbx

fun_table2:
dq set_rcx_rdi
dq clear_r8
dq xadd_instr
dq ret_r8

section .text

fun1:
  jmp set_dl_1

  mov rsp, rbp
  pop rbp
  ret

  clear_r8:
  xor r8, r8
  jmp dispatcher2

  mov rax, -8
  jmp dispatcher2

  xadd_instr:
  xadd r8, rdx
  loop xadd_instr
  jmp dispatcher2

  dispatcher2:
  add rax, 8
  jmp qword[fun_table2+rax]

  mov rax, rsi
  jmp dispatcher2

  ret_r8:
  xchg rax, r8
  ret

  set_dl_1:
  xor rax,rax
  cqo
  stc
  sete dl
  sub rax,8
  jmp dispatcher2

  add rsp, 0x28
  ret

  set_rcx_rdi:
  add rdi, rcx
  sub rcx, rdi
  neg rcx
  inc rcx
  jmp dispatcher2


fun2:
  mov rax, -8
  jmp dispatcher

  fakejmp:
  jmp +5
  db 0x75
  jmp dispatcher

  set_rbx:
  lea rbx, ZG5k3r9
  jmp dispatcher

  push_rbx:
  push rbx
  jmp dispatcher

  dispatcher:
  add rax, 8
  jmp qword[fun_table+rax]

  xor rax, rax
  mov rsp, rbp
  pop rbp
  ret

  pop_rbx:
  mov rax, rbx
  pop rbx
  ret

  rep cmpsb
  mov rsp, rbp
  pop rbp
  ret

  xlatb_instr:
  push rax
  mov al, dil
  xlatb
  mov rbx, rax
  pop rax
  jmp dispatcher


fun3:
  push rbp
  mov rbp, rsp
  sub rsp, 8
  mov qword[rbp-8], rsi

  call fun2
  mov rdi, qword[rbp-8]
  mov qword[rbp-8], rax

  call fun1
  xor rax, qword[rbp-8]
  mov rsp, rbp
  pop rbp
  ret
