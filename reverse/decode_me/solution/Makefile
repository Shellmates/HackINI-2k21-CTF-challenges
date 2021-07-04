

all:
	nasm functions.asm -felf64 -o functions.o
	gcc main.c functions.o -no-pie -o program
	strip -N fun1 -N fun2 -N fun3 -N xadd_instr -N ZG5k3r9 -N push_rbx \
        -N fakejmp -N set_rbx -N xlatb_instr -N pop_rbx -N encletter \
        -N fun_table -N dispatcher -N fun_table2 -N dispatcher2 \
        -N clear_r8 -N ret_r8 -N set_dl_1 -N set_rcx_rdi program
	rm functions.o
