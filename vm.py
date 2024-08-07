from operand import OPCode
from stack import Stack


class VM(object):
    def __init__(self, instructions: list[tuple]):
        self.instructions = instructions
        self.stack = Stack()
        self.ip = 0
        self._is_running = False
        self.instruction_handlers = {
            OPCode.PUSH: self.push,
            OPCode.POP: self.pop,
            OPCode.ADD: self.add,
            OPCode.SUB: self.sub,
            OPCode.MUL: self.mul,
            OPCode.DIV: self.div,
            OPCode.AND: self.and_,
            OPCode.OR: self.or_,
            OPCode.XOR: self.xor_,
            OPCode.NOT: self.not_,
            OPCode.EQU: self.equ,
            OPCode.JMP: self.jmp,
            OPCode.JNZ: self.jnz,
            OPCode.HALT: self.halt
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
        self.stack.push(val)

    def pop(self):
        '''
        Pops a value from the stacks and returns.
        '''
        return self.stack.pop()

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

    def and_(self):
        self.exec(lambda a, b: a & b)
    
    def or_(self):
        self.exec(lambda a,b: a | b)

    def xor_(self):
        self.exec(lambda a,b: a ^ b)

    def not_(self):
        self.push(~self.pop())

    def equ(self):
        '''
        Checks if first 2 popped values are equal.
        '''
        self.exec(lambda a,b: 1 if a == b else 0)

    def jmp(self):
        '''
        Jumps to new instruction pointer.
        '''
        new_ip = self.instructions[self.ip][1]
        self.ip = new_ip

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
        self.stack.push(fn(self.stack.pop(), self.stack.pop()))