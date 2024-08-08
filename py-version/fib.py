from vm import VM, OPCode

NOT_ONE = [
    (OPCode.PUSH, 1),
    (OPCode.SUB,),
    (OPCode.DUP,),
    (OPCode.ACALL, 3),
    (OPCode.SWP,),
    (OPCode.PUSH, 1),
    (OPCode.SUB,),
    (OPCode.ACALL, 3),
    (OPCode.ADD,),
    (OPCode.RET,),
]

NOT_ZERO = [
    (OPCode.DUP,),
    (OPCode.PUSH, 1),
    (OPCode.NEQU,),
    (OPCode.JNZ, 2),
    (OPCode.RET,),
    *NOT_ONE,
]

FIB = [
    (OPCode.DUP,),
    (OPCode.PUSH, 0),
    (OPCode.NEQU,),
    (OPCode.JNZ, 2),
    (OPCode.RET,),
    *NOT_ZERO,
]

DEMO = [
    (OPCode.PUSH, 20),
    (OPCode.CALL, 2),
    (OPCode.HALT,),
    *FIB,
]

VM(DEMO, False).interpret()