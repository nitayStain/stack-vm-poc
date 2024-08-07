#include <stdio.h>
#include "vm.h"

const struct instruction_t FIB[] = {
    // DEMO
    {.op = PUSH, .param = 20},
    {.op = CALL, .param = 2},
    {.op = HALT},

    // FIB
    {.op = DUP},
    {.op = PUSH, .param = 0},
    {.op = NEQU},
    {.op = JNZ, .param = 2},
    {.op = RET},

    // NOT_ZERO
    {.op = DUP},
    {.op = PUSH, .param = 1},
    {.op = NEQU},
    {.op = JNZ, .param = 2},
    {.op = RET},

    // NOT_ONE
    {.op = PUSH, .param = 1},
    {.op = SUB},
    {.op = DUP},
    {.op = ACALL, .param = 3},
    {.op = SWP},
    {.op = PUSH, .param = 1},
    {.op = SUB},
    {.op = ACALL, .param = 3},
    {.op = ADD},
    {.op = RET}};

const struct instruction_t SIMPLE_PROG[] = {
    {.op = PUSH, .param = 20},
    {.op = DUP},
    // {.op = POP, .param = 100},
    {.op = HALT}};

int main(void)
{
    vm_t vm;
    vm_init(&vm);

    vm_interpret(&vm, FIB);

    vm_free(&vm);

    return 0;
}