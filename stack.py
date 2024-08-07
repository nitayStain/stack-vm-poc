class Stack(object):
    def __init__(self) -> None:
        self.__stack__ = []

    def push(self, val):
        """
        A function that pushes the value into the latest list.
        """
        self.__stack__.append(val)

    def pop(self):
        """
        A function that returns the last added item to the list
        (A stack is FIFO, first in first out)
        """
        return self.__stack__.pop()