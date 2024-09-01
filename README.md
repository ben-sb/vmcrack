# vmcrack

This repo contains a disassembler and other scripts used to solve the x86 VM challenge **vmcrack** from HackTheBox.

Read the accompanying [blog post.](https://blog.deobfuscate.io/reversing-vmcrack)

## Usage

To run the disassembler:

```
python3 src/main.py
```

There are also some scripts in the `src/scripts` folder to decode the various encoded messages within the binary.

This will create disassembly files for each virtualised function in the `output` directory. Versions of each disassembled function annotated with my analysis while solving the challenge can be found in the `output/annotated` directory.