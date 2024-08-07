import enum

# OPCode = enum.IntEnum('OPCode', 'PUSH POP ADD SUB HALT TEST OUT_STACK')

class OPCode(enum.IntEnum):
    """
    VM's Operand registry
    """
    PUSH = enum.auto()
    POP = enum.auto()
    DUP = enum.auto()
    SWP = enum.auto()

    # Arithematic
    ADD = enum.auto()
    SUB = enum.auto()
    MUL = enum.auto()
    DIV = enum.auto()
    MOD = enum.auto()

    # Binary
    BAND = enum.auto()
    BOR = enum.auto()
    BNOT = enum.auto()
    BXOR = enum.auto()

    # Logical
    LAND = enum.auto()
    LOR = enum.auto()
    LNOT = enum.auto()
    EQU = enum.auto()

    # Functional
    CALL = enum.auto()
    RET = enum.auto()

    # Conditional
    JMP = enum.auto()
    JNZ = enum.auto()

    # utils
    HALT = enum.auto()
    OUT_STACK = enum.auto()
    OP_COUNT = enum.auto()
