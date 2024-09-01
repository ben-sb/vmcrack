from enum import Enum

class OperandSize(Enum):
    BYTE = 'byte'
    WORD = 'word'
    DWORD = 'dword'

    def __str__(self) -> str:
        return self.value

class Reg(Enum):
    CUSTOM = 'custom_reg'
    EAX = 'eax'
    ECX = 'ecx'
    EDX = 'edx'
    EBX = 'ebx'
    ESP = 'esp'
    EBP = 'ebp'
    ESI = 'esi'
    EDI = 'edi'
    EFLAGS = 'eflags'

    def __str__(self) -> str:
        return self.value
    
reg_mappings = {
    0x0: Reg.CUSTOM,
    0x4: Reg.EAX,
    0x8: Reg.ECX,
    0xc: Reg.EDX,
    0x10: Reg.EBX,
    0x14: Reg.ESP,
    0x18: Reg.EBP,
    0x1c: Reg.ESI,
    0x20: Reg.EDI,
    0x24: Reg.EFLAGS
}

def get_register_name(reg: Reg, size: OperandSize) -> str:
    if size != OperandSize.DWORD and (reg == Reg.EAX or reg == Reg.EBX or reg == Reg.ECX or reg == Reg.EDX):
        return reg.value[1] + 'l' if size == OperandSize.BYTE else reg.value[1:]
    else:
        return reg.value

class Operand:
    def __init__(self, value: any, size: OperandSize = None) -> None:
        self.value = value
        self.size = size
        self.is_indirect = False
        self.prefix = None

    def __str__(self) -> str:
        if isinstance(self.value, Reg):
            formatted_value = get_register_name(self.value, self.size)
        elif isinstance(self.value, int):
            formatted_value = hex(self.value)
        else:
            formatted_value = str(self.value)

        value = self.prefix + ':' + formatted_value if self.prefix else formatted_value
        value = f'[{value}]' if self.is_indirect else value
        return f'{self.size} {value}' if self.size else str(value)

class BinaryExpression:
    def __init__(self, operator: str, left: Reg | int, right: Reg | int) -> None:
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self) -> str:
        left = hex(self.left) if isinstance(self.left, int) else str(self.left)
        right = hex(self.right) if isinstance(self.right, int) else str(self.right)
        return f'{left}{self.operator}{right}'