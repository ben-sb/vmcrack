0x41a000:	jmp          0x41a010

0x41a006:	xor          dword eax, dword eax
0x41a00d:	ret          

0x41a010:	mov          dword ecx, [fs:0x30]
0x41a019:	mov          dword eax, byte [ecx+0x2]
0x41a026:	test         dword eax, dword eax
0x41a02d:	jnz          0x41a006

0x41a033:	mov          dword eax, dword [ecx+0x68]
0x41a040:	and          dword eax, 0x70
0x41a049:	cmp          dword eax, 0x70
0x41a052:	jz           0x41a006

0x41a058:	mov          dword edx, dword [ecx+0x18]
0x41a065:	mov          dword eax, dword [edx+0x40]
0x41a072:	test         dword eax, 0x2
0x41a07b:	jz           0x41a006

0x41a081:	mov          dword eax, dword [edx+0x44]
0x41a08e:	test         dword eax, dword eax
0x41a095:	jnz          0x41a006

0x41a09b:	mov          dword ecx, [gs:0x60]
0x41a0a4:	mov          dword eax, byte [ecx+0x2]
0x41a0b1:	test         dword eax, dword eax
0x41a0b8:	jnz          0x41a006

0x41a0be:	mov          dword eax, dword [ecx+0xbc]
0x41a0cb:	and          dword eax, 0x70
0x41a0d4:	cmp          dword eax, 0x70
0x41a0dd:	jz           0x41a006

0x41a0e3:	mov          dword edx, dword [ecx+0x30]
0x41a0f0:	mov          dword eax, dword [edx+0x70]
0x41a0fd:	test         dword eax, 0x2
0x41a106:	jz           0x41a006

0x41a10c:	mov          dword eax, dword [edx+0x74]
0x41a119:	test         dword eax, dword eax
0x41a120:	jnz          0x41a006

0x41a126:	push         dword esi
0x41a12a:	push         dword edi
0x41a12e:	push         0x0
0x41a134:	mov          dword eax, dword esp
0x41a13b:	push         0x6f75666d
0x41a141:	push         0x3d20392e
0x41a147:	push         0x296f3d20
0x41a14d:	push         0x3f6f3c23
0x41a153:	push         0x2e263b21
0x41a159:	push         0x2a2b2a3d
0x41a15f:	push         0xc6d672a
0x41a165:	push         0x3b2e233c
0x41a16b:	push         0x212e3d1b
0x41a171:	push         0x75751200
0x41a177:	push         0x661212e
0x41a17d:	push         0x223a0714
0x41a183:	mov          dword ecx, dword eax
0x41a18a:	sub          dword ecx, dword esp
0x41a191:	xor          byte [esp+ecx-0x1], 0x4f
0x41a1a0:	dec          dword ecx
0x41a1a4:	jnz          0x41a191

0x41a1aa:	mov          dword eax, dword esp
0x41a1b1:	push         stdout
0x41a1b7:	push         dword eax
0x41a1bb:	call         fputs
0x41a1c1:	add          esp, 0x3c
0x41a1c4:	sub          esp, 0x100
0x41a1c7:	mov          dword eax, dword esp
0x41a1ce:	push         0x0
0x41a1d4:	push         0x100
0x41a1da:	push         dword eax
0x41a1de:	call         fgets
0x41a1e4:	add          esp, 0xc
0x41a1e7:	xor          dword eax, dword eax
0x41a1ee:	mov          dword ecx, 0xffff
0x41a1f7:	mov          dword edi, dword esp
0x41a1fe:	repne scasb  byte [edi]
0x41a200:	sub          dword ecx, 0xffff
0x41a209:	not          dword ecx
0x41a20d:	dec          dword ecx
0x41a211:	mov          byte [esp+ecx], 0x0
0x41a220:	mov          dword edx, dword ecx
0x41a227:	mov          dword esi, dword esp
0x41a22e:	mov          dword edi, credential_dest_ptr
0x41a237:	rep movsb    byte [edi], byte [esi]
0x41a239:	mov          dword ecx, dword edx
0x41a240:	jmp          0x41a25d

0x41a246:	mov          dword eax, 0x1
0x41a24f:	add          esp, 0x100
0x41a252:	pop          dword edi
0x41a256:	pop          dword esi
0x41a25a:	ret          

0x41a25d:	cmp          dword edx, 0x3b
0x41a266:	jnz          0x41a246

0x41a26c:	mov          dword eax, byte [esp+ecx]
0x41a279:	inc          byte [esp+ecx-0x1]
0x41a283:	rol          byte [esp+ecx-0x1], 0x9f
0x41a292:	sub          byte [esp+ecx-0x1], 0xe
0x41a2a1:	not          byte [esp+ecx-0x1]
0x41a2ab:	xor          byte [esp+ecx-0x1], 0xc3
0x41a2ba:	neg          byte [esp+ecx-0x1]
0x41a2c4:	add          byte [esp+ecx-0x1], 0x3e
0x41a2d3:	ror          byte [esp+ecx-0x1], 0x1d
0x41a2e2:	dec          byte [esp+ecx-0x1]
0x41a2ec:	xor          byte [esp+ecx-0x1], byte al
0x41a2f9:	dec          dword ecx
0x41a2fd:	jnz          0x41a26c

0x41a303:	mov          dword edi, dword esp
0x41a30a:	push         0x17edf5
0x41a310:	push         -0x120a120b
0x41a316:	push         -0x5a2a2902
0x41a31c:	push         -0x29012902
0x41a322:	push         -0x3d3e6e9a
0x41a328:	push         0x5a32066e
0x41a32e:	push         0x6d29692d
0x41a334:	push         0x2e6a7236
0x41a33a:	push         0x35093565
0x41a340:	push         -0x758fac85
0x41a346:	push         0xff8acdc
0x41a34c:	push         -0x6f98a458
0x41a352:	push         -0xc575fe1
0x41a358:	push         -0x773c7059
0x41a35e:	push         -0x40146374
0x41a364:	mov          dword esi, dword esp
0x41a36b:	mov          dword ecx, dword edx
0x41a372:	rep cmpsb    byte [esi], byte [edi]
0x41a374:	add          esp, 0x3c
0x41a377:	jnz          0x41a246

0x41a37d:	mov          dword eax, 0x2
0x41a386:	jmp          0x41a24f
