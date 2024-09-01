0x41a3c0:	push         dword ebp
0x41a3c4:	mov          dword ebp, dword esp
0x41a3cb:	sub          esp, 0xc
0x41a3ce:	mov          dword [esp], credential_dest_ptr_2
0x41a3dd:	mov          dword [esp+0x4], encrypted_string_ptr
0x41a3ec:	mov          dword [esp+0x8], constant_0x570
0x41a3fb:	push         dword edi
0x41a3ff:	push         dword esi
0x41a403:	push         dword ebx
0x41a407:	xor          dword eax, dword eax
0x41a40e:	mov          dword ecx, 0xffff
0x41a417:	mov          dword edi, dword [ebp-0xc]
0x41a424:	repne scasb  byte [edi]
0x41a426:	sub          dword ecx, 0xffff
0x41a42f:	not          dword ecx
0x41a433:	mov          dword ebx, dword ecx
0x41a43a:	sub          esp, 0x10
0x41a43d:	mov          dword esi, dword esp
0x41a444:	push         dword esi
0x41a448:	push         dword ebx
0x41a44c:	push         dword [ebp-0xc]
0x41a456:	call         md5_func
0x41a45c:	add          esp, 0xc
0x41a45f:	sub          esp, 0x20
0x41a462:	mov          dword edi, dword esp
0x41a469:	push         dword edi
0x41a46d:	push         dword ebx
0x41a471:	push         dword [ebp-0xc]
0x41a47b:	call         sha256_func
0x41a481:	add          esp, 0xc
0x41a484:	push         dword esi
0x41a488:	push         dword edi
0x41a48c:	push         dword [ebp-0x4]
0x41a496:	push         dword [ebp-0x8]
0x41a4a0:	call         some_decryption_func
0x41a4a6:	add          esp, 0x40
0x41a4a9:	push         dword [ebp-0x4]
0x41a4b3:	push         dword [ebp-0x8]
0x41a4bd:	call         crc_func
0x41a4c3:	add          esp, 0x8
0x41a4c6:	mov          dword ebx, dword eax
0x41a4cd:	xor          dword eax, dword eax
0x41a4d4:	cmp          dword ebx, 0x4da2c9f6
0x41a4dd:	jnz          0x41a4ec

0x41a4e3:	mov          dword eax, 0x1
0x41a4ec:	pop          dword ebx
0x41a4f0:	pop          dword esi
0x41a4f4:	pop          dword edi
0x41a4f8:	add          esp, 0xc
0x41a4fb:	pop          dword ebp
0x41a4ff:	ret          
