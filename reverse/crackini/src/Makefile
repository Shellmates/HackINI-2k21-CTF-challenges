all:
	nasm -felf64 shellcode.asm -o shellcode.o
	objcopy -O binary -j .text shellcode.o shellcode
	python3 makechall.py
	echo "Shellcode size: `wc -c shellcode|cut -d' ' -f1`"
	rm -f shellcode.o shellcode
	gcc crackini.c -ocrackini
	strip crackini
	mv crackini ../challenge
