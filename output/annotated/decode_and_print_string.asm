0x41a508:	push         dword ebp
0x41a50c:	mov          dword ebp, dword esp
0x41a513:	sub          esp, 0x8

0x41a516:	mov          dword [esp], encoded_string_ptr
0x41a525:	mov          dword [esp+0x4], string_decoding_key

0x41a534:	push         dword edi
0x41a538:	push         dword esi
0x41a53c:	push         dword ebx

0x41a540:	xor          dword eax, dword eax
0x41a547:	mov          dword ecx, 0xffff                  ; read max 65535 chars
0x41a550:	mov          dword edi, dword [ebp-0x8]         ; ebp-0x8 is encoded_string_ptr
0x41a55d:	repne scasb  byte [edi]                         ; read chars until we find a zero (end of string)
0x41a55f:	sub          dword ecx, 0xffff                  ; -1 * num_chars_read
0x41a568:	not          dword ecx                          ; length of encoded_string_ptr (index of zero byte)

0x41a56c:	xor          dword edx, dword edx               ; i = 0
0x41a573:	mov          dword esi, dword ebp
0x41a57a:	sub          dword esi, 0x4
0x41a583:	mov          dword edi, dword [ebp-0x8]         ; encoded_string_ptr
0x41a590:	xor          dword ebx, dword ebx               ; j = 0

0x41a597:	cmp          dword ebx, 0x4
0x41a5a0:	jz           0x41a590                           ; j %= 4

0x41a5a6:	mov          byte al, byte [esi+ebx]            ; *(string_decoding_key)[j]
0x41a5b3:	inc          dword ebx                          ; j++
0x41a5b7:	xor          byte [edi+edx], byte al            ; *(encoded_string_ptr)[i] ^= *(string_decoding_key)[j]
0x41a5c4:	add          byte [edi+edx], 0x7c               ; *(encoded_string_ptr)[i] += -x7c
0x41a5d3:	inc          dword edx                          ; i++
0x41a5d7:	cmp          dword edx, dword ecx
0x41a5de:	jnz          0x41a597                           ; loop until i = length of encoded_string_ptr

0x41a5e4:	push         dword edi
0x41a5e8:	call         puts                               ; print decoded string
0x41a5ee:	add          esp, 0x4

0x41a5f1:	pop          dword ebx
0x41a5f5:	pop          dword esi
0x41a5f9:	pop          dword edi
0x41a5fd:	xor          dword eax, dword eax
0x41a604:	add          esp, 0x8
0x41a607:	pop          dword ebp
0x41a60b:	ret          
