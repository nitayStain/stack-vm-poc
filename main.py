from vm import VM, OPCode

PROGRAM = [
    (OPCode.PUSH, 1),
    (OPCode.PUSH, 40),
    (OPCode.EQU,),
    # (OPCode.OUT_STACK,),
    (OPCode.HALT,),
]

VM(PROGRAM).interpret()