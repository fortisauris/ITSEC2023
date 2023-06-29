## hello.a

## Hello World

section	.text
	global _start       ;must be declared for using gcc
_start:                     ;tell linker entry point
	mov	edx, len    ;dlzka spravy
	mov	ecx, msg    ;sprava na zapisanie
	mov	ebx, 1	    ;co s tym (stdout)
	mov	eax, 4	    ;systemove volanie (sys_write)
	int	0x80        ;zavolaj kernel a vykonaj
	mov	eax, 1	    ;systemove volanie (sys_exit)
	int	0x80        ;zavolaj kernel a vykonaj

section	.data

msg	db	'Hello, world!',0xa	;nas text ulozeny v bytoch
len	equ	$ - msg			;vypocitana dlzka naseho textu
