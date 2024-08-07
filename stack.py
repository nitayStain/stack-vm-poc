class Stack(object):
    def __init__(self) -> None:
        self._stack = []

    def push(self, val):
        """
        A function that pushes the value into the latest list.
        """
        self._stack.append(val)

    def pop(self):
        """
        A function that returns the last added item to the list
        (A stack is FIFO, first in first out)
        """
        return self._stack.pop()

    def top(self):
        """
        A function that returns the top value of the stack without popping it.
        """
        return self._stack[-1]

    def __repr__(self) -> str:
        return str(self._stack)