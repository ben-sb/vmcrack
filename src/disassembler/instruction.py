from enum import Enum
from disassembler.operand import *

class Mnemonic(Enum):
    NOP = 'nop'
    INC = 'inc'
    DEC = 'dec'
    NOT = 'not'
    NEG = 'neg'
    MUL = 'mul'
    IMUL = 'imul'
    DIV = 'div'
    IDIV = 'idiv'
    ADD = 'add'
    SUB = 'sub'
    ADC = 'adc'
    SBB = 'sbb'
    OR = 'or'
    XOR = 'xor'
    AND = 'and'
    CMP = 'cmp'
    TEST = 'test'
    SHL = 'shl'
    SAR = 'sar'
    SHR = 'shr'
    ROL = 'rol'
    ROR = 'ror'
    RCL = 'rcl'
    RCR = 'rcr'
    MOV = 'mov'
    PUSH = 'push'
    POP = 'pop'
    PUSHFD = 'pushfd'
    POPFD = 'popfd'
    JO = 'jo'
    JNO = 'jno'
    JC = 'jc'
    JNC = 'jnc'
    JZ = 'jz'
    JNZ = 'jnz'
    JA = 'ja'
    JNA = 'jna'
    JS = 'js'
    JNS = 'jns'
    JPE = 'jpe'
    JPO = 'jpo'
    JL = 'jl'
    JGE = 'jge'
    JG = 'jg'
    JLE = 'jle'
    JMP = 'jmp'
    CALL = 'call'
    RET = 'ret'
    MOVSB = 'movsb'
    MOVSW = 'movsw'
    MOVSD = 'movsd'
    CMPSB = 'cmpsb'
    CMPSW = 'cmpsd'
    CMPSD = 'cmpsd'
    LODSB = 'lodsb'
    LODSW = 'lodsw'
    LODSD = 'lodsd'
    STOSB = 'stob'
    STOSW = 'stosw'
    STOSD = 'stosd'
    SCASB = 'scasb'
    SCASW = 'scasw'
    SCASD = 'scasd'
    UD2 = 'ud2'

    def __str__(self) -> str:
        return self.value

UNARY_MNEMONIC_TABLE = [
    Mnemonic.INC, Mnemonic.DEC,
    Mnemonic.NOT, Mnemonic.NEG,
    Mnemonic.MUL, Mnemonic.IMUL,
    Mnemonic.DIV, Mnemonic.IDIV
]

BINARY_MNEMONIC_TABLE = [
    Mnemonic.ADD, Mnemonic.SUB,
    Mnemonic.ADC, Mnemonic.SBB,
    Mnemonic.OR, Mnemonic.XOR,
    Mnemonic.AND, Mnemonic.CMP,
    Mnemonic.TEST, Mnemonic.SHL,
    Mnemonic.SAR, Mnemonic.SHL, # duplicate opcode
    Mnemonic.SHR, Mnemonic.ROL,
    Mnemonic.ROR, Mnemonic.RCL,
    Mnemonic.RCR, Mnemonic.MOV
]

JUMP_MNEMONIC_TABLE = [
    Mnemonic.JO, Mnemonic.JNO,
    Mnemonic.JC, Mnemonic.JNC,
    Mnemonic.JZ, Mnemonic.JNZ,
    Mnemonic.JA, Mnemonic.JNA,
    Mnemonic.JS, Mnemonic.JNS,
    Mnemonic.JPE, Mnemonic.JPO,
    Mnemonic.JL, Mnemonic.JGE,
    Mnemonic.JG, Mnemonic.JLE,
    Mnemonic.JMP
]

CONTROL_FLOW_TRANSFER_MNEMONICS = {
    Mnemonic.JO, Mnemonic.JNO,
    Mnemonic.JC, Mnemonic.JNC,
    Mnemonic.JZ, Mnemonic.JNZ,
    Mnemonic.JA, Mnemonic.JNA,
    Mnemonic.JS, Mnemonic.JNS,
    Mnemonic.JPE, Mnemonic.JPO,
    Mnemonic.JL, Mnemonic.JGE,
    Mnemonic.JG, Mnemonic.JLE,
    Mnemonic.JMP, Mnemonic.RET
}

class Prefix(Enum):
    REP = 'rep'
    REPNE = 'repne'

    def __str__(self) -> str:
        return self.value

class Instruction:
    def __init__(self, address: int, mnemonic: Mnemonic, *operands: list[Operand]) -> None:
        self.address = address
        self.mnemonic = mnemonic
        self.operands = operands
        self.prefix: Prefix | None = None

    def __str__(self) -> str:
        operand_str = ', '.join([str(op) for op in self.operands])
        mnemonic_str = f'{str(self.prefix) + " " if self.prefix else ""}{str(self.mnemonic)}'
        return f'{hex(self.address)}:\t{mnemonic_str.ljust(13)}{operand_str}'