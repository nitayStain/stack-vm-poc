typedef enum opcode
{
    PUSH = 0,
    POP,
    DUP,
    SWP,

    // Arithematic
    ADD,
    SUB,
    MUL,
    DIV,
    MOD,

    // Binary
    BAND,
    BOR,
    BNOT,
    BXOR,

    // Logical
    LAND,
    LOR,
    LNOT,
    EQU,
    NEQU,

    // Functional
    CALL,
    ACALL,
    RET,

    // Conditional
    JMP,
    JNZ,

    // utils
    HALT,
    OUT_STACK,
    OP_COUNT,

} opcode;