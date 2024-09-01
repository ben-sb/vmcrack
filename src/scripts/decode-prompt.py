values = [
    0x6f75666d,
    0x3d20392e,
    0x296f3d20,
    0x3f6f3c23,
    0x2e263b21,
    0x2a2b2a3d,
    0xc6d672a,
    0x3b2e233c,
    0x212e3d1b,
    0x75751200,
    0x661212e,
    0x223a0714
]
values.reverse()

decoded = []
for value in values:
    decoded.append((value & 0xff) ^ 0x4f)
    decoded.append(((value >> 8) & 0xff) ^ 0x4f)
    decoded.append(((value >> 16) & 0xff) ^ 0x4f)
    decoded.append(((value >> 24) & 0xff) ^ 0x4f)

print(''.join([chr(c) for c in decoded]))

"""
[Human.IO]::Translate("Credentials por favor"):
"""