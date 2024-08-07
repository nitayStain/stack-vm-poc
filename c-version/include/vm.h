#include <stdio.h>
#include "operand.h"
#include "stack.h"

#define true 1
#define false !true

typedef unsigned char bool;

typedef stack_piece_t stack_t;

struct instruction_t
{
    opcode op;
    int param;
};

typedef struct instruction_t *instructions_t;

typedef struct vm vm_t;

typedef void (*vm_func_t)(vm_t *);
typedef int (*vm_ifunc_t)(vm_t *);
struct vm
{
    instructions_t program;

    int ip;

    stack_t *main_stack;
    stack_t *call_stack;

    bool is_running;
};

void vm_init(vm_t *vm);
void vm_interpret(vm_t *vm, instructions_t program);

void vm_push(vm_t *vm);
int vm_pop(vm_t *vm);
int vm_add(int a, int b);
int vm_sub(int a, int b);
int vm_mul(int a, int b);
int vm_div(int a, int b);
int vm_mod(int a, int b);

int vm_b_and(int a, int b);
int vm_b_or(int a, int b);
int vm_b_xor(int a, int b);
void vm_b_not(vm_t *vm);

int vm_equ(int a, int b);
int vm_nequ(int a, int b);
void vm_call(vm_t *vm);
void vm_ret(vm_t *vm);
void vm_jmp(vm_t *vm);
void vm_jnz(vm_t *vm);

void vm_dup(vm_t *vm);
void vm_swp(vm_t *vm);

void vm_halt(vm_t *vm);

typedef int (*fn_t)(int, int);
void vm_exec(vm_t *vm, fn_t fn);

void vm_free(vm_t *vm);
