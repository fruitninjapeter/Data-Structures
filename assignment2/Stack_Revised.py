class Stack:  # Stack class implemented with array
    def __init__(self, capacity, init_items=None):  # Creates an optionally empty stack with a capacity
        self.capacity = capacity  # capacity is max number of Nodes
        self.items = [None] * capacity  # array for stack
        self.num_items = 0  # number of items in stack
        if init_items is not None:  # if init_items is not None, initialize stack
            if len(init_items) > capacity:  # if the length of the init_items List exceeds capacity, raise IndexError
                raise IndexError
            else:
                self.num_items = len(init_items)
                self.items[:self.num_items] = init_items

    def __eq__(self, other):
        return ((type(other) == Stack)
                and self.capacity == other.capacity
                and self.items[:self.num_items] == other.items[:other.num_items])

    def __repr__(self):
        return "Stack({!r}, {!r})".format(self.capacity, self.items[:self.num_items])

    def is_empty(self):  # Returns True if the stack is empty, and False otherwise
        return self.num_items == 0

    def is_full(self):  # Returns True if the stack is full, and False otherwise
        return self.capacity == self.num_items

    def push(self, item):  # If stack is not full, pushes item on stack.
        if self.is_full():  # If stack is full when push is attempted, raises IndexError
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1  # increment number of items

    def pop(self):  # If stack is not empty, pops item from stack and returns item.
        if self.is_empty():  # If stack is empty when pop is attempted, raises IndexError
            raise IndexError
        data = self.items[self.num_items-1]  # list length is n - 1 (n: number of items), so top of list is n - 1
        self.items[self.num_items-1] = None
        self.num_items -= 1
        return data

    def peek(self):  # If stack is not empty, returns next item to be popped (but does not remove the item)
        if self.is_empty():  # If stack is empty, raises IndexError
            raise IndexError
        return self.items[self.num_items-1]

    def size(self):  # Returns the number of elements currently in the stack, not the capacity
        return self.num_items