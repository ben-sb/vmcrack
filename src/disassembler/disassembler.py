import struct
from typing import Dict
from .instruction import *
from .operand import *

class Disassembler:
    def __init__(self, bytecode: list[int], base_addr: int, parameters: list) -> None:
        self.bytecode = bytecode
        self.base_addr = base_addr
        self.parameter_map = self.build_parameter_map(parameters)
        self.instructions: list[Instruction] = []
        self.pos = 0

    def build_parameter_map(self, params: list) -> Dict[int, str]:
        param_map = {}
        for param in params:
            param_map[param['addr']] = param['name']
        return param_map

    def read_byte(self) -> int:
        byte = self.bytecode[self.pos]
        self.pos += 1
        return byte
    
    def peek_byte(self) -> int:
        return self.bytecode[self.pos]
    
    def read_word(self) -> int:
        word = struct.unpack('<h', self.bytecode[self.pos:self.pos + 2])[0]
        self.pos += 2
        return word
    
    def read_dword(self) -> int:
        dword = struct.unpack('<i', self.bytecode[self.pos:self.pos + 4])[0]
        self.pos += 4
        return dword

    def load_operand_size(self) -> OperandSize:
        size = self.read_byte()
        match size:
            case 1:
                return OperandSize.BYTE
            case 2:
                return OperandSize.WORD
            case 3:
                return OperandSize.DWORD
            case _:
                raise Exception(f'Unknown operand size specifier {hex(size)}')

    def load_register(self) -> Reg:
        offset = self.read_byte()
        if offset in reg_mappings:
            return reg_mappings[offset]
        else:
            raise Exception(f'Unknown VM register offset {hex(offset)}')

    def load_operand(self) -> Operand:
        addressing_type = self.read_byte()
        match addressing_type:
            # register
            case 1:
                size = self.load_operand_size()
                reg = self.load_register()
                return Operand(reg, size)

            # effective address
            case 2:
                size = self.load_operand_size()
                reg_1 = self.load_register()
                reg_2 = self.load_register()
                combine_flag = self.read_byte()
                offset = self.read_dword()

                match combine_flag:
                    case 0:
                        value = reg_1
                    case 0x1:
                        value = BinaryExpression('+', reg_1, reg_2)
                    case 0x2:
                        value = BinaryExpression('+', reg_1, BinaryExpression('*', reg_2, 2))
                    case 0x4:
                        value = BinaryExpression('+', reg_1, BinaryExpression('*', reg_2, 4))
                    case 0x8:
                        value = BinaryExpression('+', reg_1, BinaryExpression('*', reg_2, 8))
                    case _:
                        raise Exception(f'Unknown operand combination flag {combine_flag}')

                if offset > 0:
                    value = BinaryExpression('+', value, offset)
                elif offset < 0:
                    value = BinaryExpression('-', value, -offset)

                operand = Operand(value, size)
                operand.is_indirect = True
                return operand

            # immediate dword
            case 3:
                addr = self.base_addr + self.pos
                if addr in self.parameter_map:
                    self.read_dword()
                    return self.parameter_map[addr]

                value = self.read_dword()
                return Operand(value)
            
            case _:
                raise Exception(f'Unknown operand addressing type {hex(addressing_type)}')

    def add_instruction(self, instr: Instruction) -> None:
        self.instructions.append(instr)

    def get_disassembly(self) -> list[Instruction]:
        disassembly = []

        for instr in self.instructions:
            disassembly.append(str(instr))
            if isinstance(instr, Instruction) and instr.mnemonic in CONTROL_FLOW_TRANSFER_MNEMONICS:
                disassembly.append('')

        return '\n'.join(disassembly)
    
    def disassemble(self) -> None:
        while self.pos < len(self.bytecode):
            addr = self.base_addr + self.pos
            opcode = self.read_byte()

            match opcode:
                case 0:
                    self.add_instruction(Instruction(addr, Mnemonic.NOP))

                case 0x1 | 0x2 | 0x3 | 0x4 | 0x5 | 0x6 | 0x7 | 0x8:
                    mnemonic = UNARY_MNEMONIC_TABLE[opcode - 0x1]
                    operand = self.load_operand()
                    self.add_instruction(Instruction(addr, mnemonic, operand))

                case 0x9 | 0xa | 0xb | 0xc | 0xd | 0xe | 0xf | 0x10 | 0x11 | 0x12 | 0x13 | 0x14 | 0x15 | 0x16 | 0x17 | 0x18 | 0x19 | 0x1a:
                    mnemonic = BINARY_MNEMONIC_TABLE[opcode - 0x9]
                    dest = self.load_operand()
                    src = self.load_operand()
                    self.add_instruction(Instruction(addr, mnemonic, dest, src))

                case 0x1b:
                    dest = self.load_operand()
                    src = self.load_operand()
                    src.is_indirect = True
                    src.prefix = 'fs'
                    self.add_instruction(Instruction(addr, Mnemonic.MOV, dest, src))

                case 0x1c:
                    dest = self.load_operand()
                    src = self.load_operand()
                    src.is_indirect = True
                    src.prefix = 'gs' # unclear where this loads from, but from bytecode we can infer it is gs (for x64 weirdly)
                    self.add_instruction(Instruction(addr, Mnemonic.MOV, dest, src))

                case 0x1d:
                    operand = self.load_operand()
                    self.add_instruction(Instruction(addr, Mnemonic.PUSH, operand))

                case 0x1e:
                    operand = self.load_operand()
                    self.add_instruction(Instruction(addr, Mnemonic.POP, operand))

                case 0x1f:
                    self.add_instruction(Instruction(addr, Mnemonic.PUSHFD))

                case 0x20:
                    self.add_instruction(Instruction(addr, Mnemonic.POPFD))

                case 0x21 | 0x22 | 0x23 | 0x24 | 0x25 | 0x26 | 0x27 | 0x28 | 0x29 | 0x2a | 0x2b | 0x2c | 0x2d | 0x2e | 0x2ef | 0x30 | 0x31:
                    operand = self.load_operand()
                    if not isinstance(operand.value, int):
                        raise Exception(f'Can not resolve jump offset')
                
                    target = self.base_addr + self.pos + operand.value
                    mnemonic = JUMP_MNEMONIC_TABLE[opcode - 0x21]
                    self.add_instruction(Instruction(addr, mnemonic, Operand(target)))

                case 0x32:
                    operand = self.load_operand()
                    self.add_instruction(Instruction(addr, Mnemonic.CALL, operand))

                case 0x33:
                    self.read_word() # seems to be unused
                    self.add_instruction(Instruction(addr, Mnemonic.RET))

                case 0x34:
                    amount = self.read_word()
                    self.add_instruction(Instruction(addr, Mnemonic.ADD, Operand(Reg.ESP), Operand(amount)))

                case 0x35:
                    amount = self.read_word()
                    self.add_instruction(Instruction(addr, Mnemonic.SUB, Operand(Reg.ESP), Operand(amount)))

                case 0x36:
                    size = self.load_operand_size()
                    mnemonic = f'movs{str(size)[0]}'

                    dest = Operand(Reg.EDI, size)
                    dest.is_indirect = True

                    src = Operand(Reg.ESI, size)
                    src.is_indirect = True

                    self.add_instruction(Instruction(addr, Mnemonic(mnemonic), dest, src))

                case 0x37:
                    size = self.load_operand_size()
                    mnemonic = f'movs{str(size)[0]}'

                    dest = Operand(Reg.EDI, size)
                    dest.is_indirect = True

                    src = Operand(Reg.ESI, size)
                    src.is_indirect = True

                    instr = Instruction(addr, Mnemonic(mnemonic), dest, src)
                    instr.prefix = 'rep'
                    self.add_instruction(instr)

                case 0x38:
                    size = self.load_operand_size()
                    mnemonic = f'cmps{str(size)[0]}'

                    dest = Operand(Reg.ESI, size)
                    dest.is_indirect = True

                    src = Operand(Reg.EDI, size)
                    src.is_indirect = True

                    self.add_instruction(Instruction(addr, Mnemonic(mnemonic), dest, src))

                case 0x39:
                    size = self.load_operand_size()
                    mnemonic = f'cmps{str(size)[0]}'

                    dest = Operand(Reg.ESI, size)
                    dest.is_indirect = True

                    src = Operand(Reg.EDI, size)
                    src.is_indirect = True

                    instr = Instruction(addr, Mnemonic(mnemonic), dest, src)
                    instr.prefix = 'rep'
                    self.add_instruction(instr)

                case 0x3a:
                    size = self.load_operand_size()
                    mnemonic = f'cmps{str(size)[0]}'

                    dest = Operand(Reg.ESI, size)
                    dest.is_indirect = True

                    src = Operand(Reg.EDI, size)
                    src.is_indirect = True

                    instr = Instruction(addr, Mnemonic(mnemonic), dest, src)
                    instr.prefix = 'repne'
                    self.add_instruction(instr)

                case 0x3b:
                    size = self.load_operand_size()
                    mnemonic = f'lods{str(size)[0]}'

                    operand = Operand(Reg.ESI, size)
                    operand.is_indirect = True

                    self.add_instruction(Instruction(addr, Mnemonic(mnemonic), operand))

                case 0x3c:
                    size = self.load_operand_size()
                    mnemonic = f'stos{str(size)[0]}'

                    operand = Operand(Reg.EDI, size)
                    operand.is_indirect = True

                    self.add_instruction(Instruction(addr, Mnemonic(mnemonic), operand))

                case 0x3d:
                    size = self.load_operand_size()
                    mnemonic = f'scas{str(size)[0]}'

                    operand = Operand(Reg.EDI, size)
                    operand.is_indirect = True

                    instr = Instruction(addr, Mnemonic(mnemonic), operand)
                    instr.prefix = 'rep'
                    self.add_instruction(instr)

                case 0x3e:
                    size = self.load_operand_size()
                    mnemonic = f'scas{str(size)[0]}'

                    operand = Operand(Reg.EDI, size)
                    operand.is_indirect = True

                    instr = Instruction(addr, Mnemonic(mnemonic), operand)
                    instr.prefix = 'repne'
                    self.add_instruction(instr)

                case 0x40:
                    size = self.load_operand_size()
                    mnemonic = f'stos{str(size)[0]}' # stos but doesn't put eflags back onto stack

                    operand = Operand(Reg.EDI, size)
                    operand.is_indirect = True

                    self.add_instruction(Instruction(addr, Mnemonic(mnemonic), operand))

                case 0x41:
                    # this instruction checks if TIB->StackBase > TIB->StackLimit
                    # and if so decreases the stack base until it is not,
                    # but it always unconditionally divides by zero so we use UD2
                    self.add_instruction(Instruction(addr, Mnemonic.UD2))

                case _:
                    raise Exception(f'Unknown opcode {hex(opcode)}')