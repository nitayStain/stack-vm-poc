from vm import VM, OPCode

DEMO = [
    (OPCode.PUSH, 1),
    (OPCode.PUSH, 40),
    (OPCode.EQU,),
    (OPCode.JNZ, 4),
    (OPCode.PUSH, 80),
    (OPCode.PUSH, 120),
    (OPCode.ADD,),
    (OPCode.HALT,),
]

VM(DEMO, True).interpret()