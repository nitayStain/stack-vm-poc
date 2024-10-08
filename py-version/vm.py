from operand import OPCode
import time

class VM(object):
    def __init__(self, instructions: list[tuple], debug = False):
        self.instructions = instructions
        self.stack = []
        self.call_stack = []
        self.ip = 0
        self._is_running = False
        self.debug = debug

        self.instruction_handlers = {
            OPCode.PUSH:        self.push,
            OPCode.POP:         self.pop,
            OPCode.DUP:         self.dup,
            OPCode.SWP:         self.swp,
            OPCode.ROT:         self.rot,
            OPCode.ADD:         self.add,
            OPCode.SUB:         self.sub,
            OPCode.MUL:         self.mul,
            OPCode.DIV:         self.div,
            OPCode.BAND:        self.b_and,
            OPCode.BOR:         self.b_or,
            OPCode.BXOR:        self.b_xor,
            OPCode.BNOT:        self.b_not,
            OPCode.LAND:        self.l_and,
            OPCode.LOR:         self.l_or,
            OPCode.LNOT:        self.l_not,
            OPCode.EQU:         self.equ,
            OPCode.NEQU:        self.nequ,
            OPCode.CALL:        self.call,
            OPCode.ACALL:       self.acall,
            OPCode.RET:         self.ret,
            OPCode.JMP:         self.jmp,
            OPCode.JNZ:         self.jnz,
            OPCode.OUT_STACK:   lambda: print(self.stack),
            OPCode.HALT:        self.halt
        }

    def interpret(self):
        '''
        Interprets the instruction set that was given in the constructor.
        '''
        self._is_running = len(self.instructions) > 0
        while self._is_running:
            try:
                op = self.instructions[self.ip][0]
            except IndexError:
                print("Unknown Instruction pointer, halting.")
                self.halt()
                break

            self.trace('Current stack:', self.stack)
            self.trace(f'Running instruction {op.name} | ip: {self.ip}')

            if op not in self.instruction_handlers:
                assert False, "Support for operand {} doesn't exist".format(op.name)
            else:
                self.instruction_handlers[op]()

            self.ip += 1

    def push(self):
        '''
        Pushes a value to the stack
        '''
        val = self.instructions[self.ip][1]
        self.stack.append(val)

    def pop(self):
        '''
        Pops a value from the stacks and returns.
        '''
        return self.stack.pop()

    def dup(self):
        '''
        Duplicates the top of the stack.
        '''
        self.stack.append(self.stack[-1])

    def swp(self):
        '''
        Swaps the first 2 popped values.
        '''
        a, b = (self.stack.pop(), self.stack.pop())
        self.stack.append(a)
        self.stack.append(b)

    def rot(self):
        '''
        Swaps the given index to the top of the stack
        '''
        self.stack.append(self.stack.pop(-self.stack.pop()))

    def add(self):
        '''
        Appends 2 first popped values.
        '''
        self.exec(lambda a,b: a + b)

    def sub(self):
        '''
        Substructs 2 first popped values.
        '''
        self.exec(lambda a,b: b - a)

    def mul(self):
        '''
        Multiplies 2 first popped values.
        '''
        self.exec(lambda a,b: a * b)

    def div(self):
        '''
        Divides first 2 popped values.
        '''
        self.exec(lambda a, b: b / a)

    def mod(self):
        '''
        Performs a modulo operation.
        '''
        self.exec(lambda a, b: b % a)

    def b_and(self):
        '''
        Performs an AND operation on the 2 popped values.
        '''
        self.exec(lambda a, b: a & b)

    def b_or(self):
        '''
        Performs an OR operation on the 2 popped values.
        '''
        self.exec(lambda a,b: a | b)

    def b_xor(self):
        '''
        Performs a XOR operation on the 2 popped values.
        '''
        self.exec(lambda a,b: a ^ b)

    def b_not(self):
        '''
        Performs a NOT operation on the 2 popped values.
        '''
        self.stack[-1] = ~self.stack[-1]

    def l_and(self):
        '''
        Performs a logical And operation on the 2 popped values.
        '''
        self.exec(lambda a,b: a and b)

    def l_or(self):
        '''
        Performs a logical Or operation on the 2 popped values.
        '''
        self.exec(lambda a,b: a or b)

    def l_not(self):
        '''
        Performs a logical not operation on the top value.
        '''
        self.push(not self.pop())

    def equ(self):
        '''
        Checks if first 2 popped values are equal.
        '''
        self.exec(lambda a,b: 1 if a == b else 0)

    def nequ(self):
        '''
        Performs a not-equal operation.
        '''
        self.exec(lambda a,b: 1 if a != b else 0)

    def call(self):
        '''
        A call instruction pushes the current ip to the stack, and jumps to the given ip.
        '''
        self.call_stack.append(self.ip)
        self.jmp()

    def acall(self):
        self.call_stack.append(self.ip)
        self.ip = self.instructions[self.ip][1] - 1

    def ret(self):
        '''
        A ret instruction takes the top, that should be the ip that was pushed by the call instruction
        '''
        self.ip = self.call_stack.pop()

    def jmp(self):
        '''
        Jumps to new instruction pointer.
        '''
        new_ip = self.instructions[self.ip][1]
        self.ip += new_ip - 1 # used to make the provided instruction pointer more readable

    def jnz(self):
        '''
        Jumps if the last flag (FIFO) is not zero.
        '''
        if self.pop() != 0:
            self.jmp()

    def halt(self):
        '''
        Halts. (Kills the program basically)
        '''
        self._is_running = False

    def exec(self, fn):
        '''
        Executes a lambda function on 2 first values.
        '''
        self.stack.append(fn(self.stack.pop(), self.stack.pop()))

    def trace(self, *args):
        if self.debug:
            print("[INFO]: ", *args)