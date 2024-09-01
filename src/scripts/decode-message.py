def decode(data, key):
    encoded = ''
    key_bytes = int.to_bytes(key, length=4, byteorder='little')

    for i in range(0, len(data)):
        key_byte = key_bytes[i % 4]
        xored = data[i] ^ key_byte
        xored = (xored + 0x7c) % 0x100
        if xored > 127:
            xored -= 256
        encoded += chr(xored)

    return encoded

# call in TLS callback for remote debugger check
data = bytes.fromhex('360d375e190d36170c176a1f4f0527171d166a0d18073c124f193d0b060c255e1807365e18146a0207176a120204231d024e6a0d185a3309125a36161d0d355e06066a1f101b335e060c6a10021b385f')
key = 0xfacefeeb
print(decode(data, key))
"""
You notice a weird sound coming out of the device, so you throw it away in fear!
"""

# call in TLS callback for NtQueryInformationProcess
data = bytes.fromhex('c8584b4ce0174142a90a4452a90c4051e1040953fc155b51e40b0950fb0f5c1ef510441ee5155757ea151f08bf584042a9115a1ee80b0957e7584042a9115a1efa1b4848ff115f51a9055a08bf4e0977d5587c63da240976c826641ec5357573ca246472a9257a08bf4e1f1edb257f1fa85923')
key = 0xbaadfc0d
print(decode(data, key))
"""
A bright red light emerges from the device... it is as if it is scanning us... IT MUST HAVE DETECTED US.... RUN!!!
"""

# call in TLS callback for hide from debugger
data = bytes.fromhex('d0b18564ffb1842deaab9464f5ae9564e5ab862deaabd838fbbf9132e6e68433a9aa8a2dfdb2d82df5b59530e7e69132f5b1d838e1abd82bfbb18532e5e69932e5e68b38feb68829e5e69138a9f3d838e1abd828e4b89127e4e68b29fda8cd28e4b58436f4a58429e5e69132a9aa952ae4b08b29bff0ce')
key = 0xc07c420d
print(decode(data, key))
"""
You noticed the device trying to drill itself into the ground and stopped it - the device self-destructed in defense...
"""

# first call in logic_1
data = bytes.fromhex('2626e4541623f71d1923a906173ae4150923e5541b6ee7090837a903146ef919083be81a0839fa084e6ee802166ee40a173cf0081227ff1b5a31e0081227ff541b6eb8445a3be4080823a9061b22e009096ee7060d34e4540939fd1d1678bf425a27ff170e33e51d0c21a90d0d33bf424c')
key = 0xf00dcafe
print(decode(data, key))
"""
The device released a fury of permafrost, and everything within a 10 metre radius froze solid... including you...
"""

# first call in logic_2
data = bytes.fromhex('324d547a1d4d5533085709291c4f442603535f354b454433195609320a4a59371d535f354b535f7a1752447a0757573308571f6c5d1a6006381a687a3768680a4a1a68183c68757a3e737a09226d7f7b4b7b6b0d3966087b')
key = 0xdeadbeef
print(decode(data, key))
"""
You notice something weird happening in the device... ITS A TRAP! ABORT MISSION! ABORT!!
"""

# second call (first set of possible parameters) in logic_2
data = bytes.fromhex('fd2f010fcd2a1246c22a4c5cdd350d46ce2f100fdc374c5dcc29115ccc344c53d6671e42d2371b59cd671058813e1b5297714c73e90a4c63ec053160ee0e3a60810e3f0ffe0a2d64810e3a0ffd0f257c81103a6280')
key = 0xabe8c325
print(decode(data, key))
"""
The device straight up refuses to respond to you.. THE DEBUGGING IS WEAK IN THIS ONE!
"""

# second call (second set of possible parameters) in logic_2
data = bytes.fromhex('f936939acd3792d7d22c829ac1618dc8cd2d83ccdc288fce802098d6803d86d7802d83c4c922839ad42881d2dc2c829add31da9ac23c929ad63692d2c937819ac8209ecacd3783d69677d89ad52097d8cd6187c68f32ced8d23685d7d606')
key = 0x3e6ac524
print(decode(data, key))
"""
You entered a credential and the device lighted up, but nothing happened... maybe it's broken?
"""

# third call in logic_2
# data = bytes.fromhex('2e2a8761c8ac9189bcfc7cfd4be7695e58841ef338a9e658bdae6a73d30a6ca8e7fd03c33c73cfdd034a98dd6d8def4d8e974aea04630c8f48483de23774d061a7abff67c2ab3d0622554252e722485c619b56581b7a63d8c8d843069fe293faaae3ebe4afd6ee8e730511f914ddd783d02d394aa396cdc787afe2f8a7e864b88c6cab995e767656924e1f5e')
# key = 0xc1c1c1c1
# print(decode(data, key))
# this seems to decode wrong, think the data is modified by other functions at runtime

# fourth and last call in logic_2
# data = bytes.fromhex('20b504156f0368c5d669bd7cbda7041020e1e69e22bfa59e34e1e6886babf0db6fbaa5db22abb8c522a2b1cb6abea6c522bea38860a5a7c36fa1e69e34')
# key = 0x2c545386
# print(decode(data, key))
# this also seems to decode wrong, think the data is modified by other functions at runtime