values = [
    0x17edf5,
    -0x120a120b,
    -0x5a2a2902,
    -0x29012902,
    -0x3d3e6e9a,
    0x5a32066e,
    0x6d29692d,
    0x2e6a7236,
    0x35093565,
    -0x758fac85,
    0xff8acdc,
    -0x6f98a458,
    -0xc575fe1,
    -0x773c7059,
    -0x40146374
]
values.reverse()

chars = []
for value in values:
    chars.append(value & 0xff)
    chars.append((value >> 8) & 0xff)
    chars.append((value >> 16) & 0xff)
    chars.append((value >> 24) & 0xff)

def ror(x, n):
    n %= 8
    return ((x >> n) | (x << (8 - n))) & 0xff

def rol(x, n):
    n %= 8
    return ((x << n) | (x >> (8 - n))) & 0xff

i = 0
while i < len(chars) - 1:
    char = chars[i]
    next_char = chars[i + 1]

    char = (char ^ next_char) & 0xff
    char = (char + 1) & 0xff
    char = rol(char, 0x1d)
    char = (char - 0x3e) & 0xff
    char = (-char) % 256 # neg
    char = (char ^ 0xc3) & 0xff
    char = (~char) & 0xff # not
    char = (char + 0xe) & 0xff
    char = ror(char, 0x9f)
    char = (char - 1) & 0xff

    chars[i] = char
    i += 1

print(''.join([chr(c) for c in chars]))

"""
[Alien.IO]::Translate("Skrr pip pop udurak reeeee skiiiii")

Providing this to vmcrack outputs

HTB{V1RTU4L_M4CH1N35_G035_BRRRRRR!11!1!1!}
"""