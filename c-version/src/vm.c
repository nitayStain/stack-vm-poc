#include "vm.h"
#include <stdlib.h>

void vm_init(vm_t *vm)
{
    vm->call_stack = (stack_t *)malloc(sizeof(stack_t));
    if (vm->call_stack == NULL)
    {
        printf("Cannot initialize the call stack.\n");
        return;
    }

    vm->main_stack = (stack_t *)malloc(sizeof(stack_t));
    vm->is_running = false;
    vm->ip = 0;
}

// runs the program, executes every instruction and manipulates the Ip correctly.
void vm_interpret(vm_t *vm, instructions_t program)
{
    vm->program = program;
    vm->is_running = program != NULL;
    while (vm->is_running)
    {
        if (vm->ip < 0 || vm->program[vm->ip].op >= OP_COUNT)
        {
            printf("Unknown instruction pointer, halting.\n");
            vm_halt(vm);
            continue;
        }

        printf("Current stack: ");
        s_print(vm->main_stack);
        printf("Running instruction, ip %d\n", vm->ip);

        opcode op = vm->program[vm->ip].op;
        switch (op)
        {
        case PUSH:
            vm_push(vm);
            break;
        case POP:
            vm_pop(vm);
            break;
        case HALT:
            vm_halt(vm);
            break;
        case ADD:
            vm_exec(vm, vm_add);
            break;
        case SUB:
            vm_exec(vm, vm_sub);
            break;
        case MUL:
            vm_exec(vm, vm_mul);
            break;
        case DIV:
            vm_exec(vm, vm_div);
            break;
        case MOD:
            vm_exec(vm, vm_mod);
            break;
        case DUP:
            vm_dup(vm);
            break;
        case SWP:
            vm_swp(vm);
            break;
        case BAND:
            vm_exec(vm, vm_b_and);
            break;
        case BOR:
            vm_exec(vm, vm_b_or);
            break;
        case BXOR:
            vm_exec(vm, vm_b_xor);
            break;
        case BNOT:
            vm_b_not(vm);
            break;
        case EQU:
            vm_exec(vm, vm_equ);
            break;
        case NEQU:
            vm_exec(vm, vm_nequ);
            break;
        case CALL:
            vm_call(vm);
            break;
        case ACALL:
            vm_acall(vm);
            break;
        case RET:
            vm_ret(vm);
            break;
        case JMP:
            vm_jmp(vm);
            break;
        case JNZ:
            vm_jnz(vm);
            break;
        default:
            printf("Support for operand %d doesn't exist.\n", op);
            vm_halt(vm);
            break;
        }

        vm->ip++;
    }
}

void vm_push(vm_t *vm)
{
    struct instruction_t inst = vm->program[vm->ip];
    s_push(&vm->main_stack, inst.param);
}

int vm_pop(vm_t *vm)
{
    return s_pop(&vm->main_stack);
}

void vm_dup(vm_t *vm)
{
    int value = vm->main_stack->data;
    s_push(&vm->main_stack, value);
}

void vm_swp(vm_t *vm)
{
    int a = s_pop(&vm->main_stack);
    int b = s_pop(&vm->main_stack);
    s_push(&vm->main_stack, a);
    s_push(&vm->main_stack, b);
}

void vm_add(int a, int b)
{
    return a + b;
}

void vm_sub(int a, int b)
{
    return b - a;
}

void vm_mul(int a, int b)
{
    return a * b;
}

void vm_div(int a, int b)
{
    return b / a;
}

void vm_mod(int a, int b)
{
    return b % a;
}

void vm_b_and(int a, int b)
{
    return a & b;
}

void vm_b_or(int a, int b)
{
    return a | b;
}

void vm_b_xor(int a, int b)
{
    return a ^ b;
}

void vm_b_not(vm_t *vm)
{
    s_push(&vm->main_stack, ~(s_pop(&vm->main_stack)));
}

void vm_l_and(int a, int b)
{
    return (bool)a && (bool)b;
}

void vm_l_or(int a, int b)
{
    return (bool)a || (bool)b;
}

// Note: add rest of logical stuff

void vm_equ(int a, int b)
{
    return a == b;
}

void vm_nequ(int a, int b)
{
    return a != b;
}

void vm_call(vm_t *vm)
{
    s_push(&vm->call_stack, vm->ip);
    vm_jmp(vm);
}

void vm_acall(vm_t *vm)
{
    s_push(&vm->call_stack, vm->ip);

    int new_ip = vm->program[vm->ip].param;
    vm->ip = new_ip - 1;
}

void vm_ret(vm_t *vm)
{
    vm->ip = s_pop(&vm->call_stack);
}

void vm_jmp(vm_t *vm)
{
    int new_ip = vm->program[vm->ip].param;
    vm->ip += new_ip - 1;
}

void vm_jnz(vm_t *vm)
{
    if (s_pop(&vm->main_stack) != 0)
    {
        vm_jmp(vm);
    }
}

void vm_halt(vm_t *vm)
{
    vm->is_running = false;
}

void vm_exec(vm_t *vm, fn_t fn)
{
    stack_t **stack = vm->main_stack;
    if (*stack == NULL || (*stack)->next == NULL)
        return;
    s_push(stack, (int)fn(s_pop(stack), s_pop(stack)));
}

void vm_free(vm_t *vm)
{
    s_free(vm->call_stack);
    s_free(vm->main_stack);
}