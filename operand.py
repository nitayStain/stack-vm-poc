import enum

# OPCode = enum.IntEnum('OPCode', 'PUSH POP ADD SUB HALT TEST OUT_STACK')

class OPCode(enum.IntEnum):
    """
    VM's Operand registry
    """
    PUSH = enum.auto()
    POP = enum.auto()

    # Arithematic
    ADD = enum.auto()
    SUB = enum.auto()
    MUL = enum.auto()
    DIV = enum.auto()

    # Binary
    AND = enum.auto()
    OR = enum.auto()
    NOT = enum.auto()
    XOR = enum.auto()
    
    # Conditional
    EQU = enum.auto()
    JMP = enum.auto()
    JNZ = enum.auto()

    # utils
    HALT = enum.auto()
    OUT_STACK = enum.auto()
    OP_COUNT = enum.auto()
