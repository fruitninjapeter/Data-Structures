# Stack class implemented with array

class Stack:    # Implements an efficient last-in first-out Abstract Data Type using a Python List
    def __init__(self, capacity, init_items=None):  # Creates an empty.txt stack with a capacity
        self.capacity = capacity        # capacity of stack
        self.items = [None]*capacity    # array for stack
        self.num_items = 0              # number of items in stack
        if init_items is not None:      # if init_items is not None, initialize stack
            if len(init_items) > capacity:
                raise IndexError    # if the length of the init_items List exceeds capacity, raise IndexError
            self.num_items = len(init_items)
            self.items[:self.num_items] = init_items

    def __eq__(self, other):
        return ((type(other) == Stack)
            and self.capacity == other.capacity
            and self.items[:self.num_items] == other.items[:other.num_items]
            )

    def __repr__(self):
        return "Stack({!r}, {!r})".format(self.capacity, self.items[:self.num_items])

    def is_empty(self):
        return self.num_items == 0  # True if the stack is empty.txt, false otherwise

    def is_full(self):
        return self.num_items == self.capacity  # True if the stack is full, false otherwise

    def push(self, item):
        if self.num_items >= self.capacity:  # if stack is full raises IndexError
            raise IndexError
        self.items[self.num_items] = item  # if stack isn't full, pushes item on stack
        self.num_items += 1

    def pop(self):
        if self.num_items == 0:  # if stack is empty.txt raises IndexError
            raise IndexError
        temp = self.items[self.num_items-1]  # Pops item from stack and returns item.
        self.num_items -= 1
        return temp

    def peek(self):
        if self.num_items == 0:  # if stack is empty.txt raises IndexError
            raise IndexError
        return self.items[:self.num_items][-1]

    def size(self):  # returns the number of elements currently in the stack, not capacity
        return self.num_items