# NodeList is one of None or Node(value, rest), where rest is reference to the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value      # object reference stored in Node
        self.rest = rest        # reference to NodeList

    def __eq__(self, other):
        return ((type(other) == Node)
          and self.value == other.value
          and self.rest == other.rest)

    def __repr__(self):
        return "Node({!r}, {!r})".format(self.value, self.rest)


class Stack:  # Implements efficient last-in first-out Abstract Data Type using a node list
    # top is the top Node of stack
    def __init__(self, top=None):
        self.top = top              # top node of stack
        self.num_items = 0          # number of items in stack
        node = top                  # set number of items based on input
        while node is not None:
            self.num_items += 1
            node = node.rest

    def __eq__(self, other):
        return ((type(other) == Stack)
          and self.top == other.top
        )

    def __repr__(self):
        return ("Stack({!r})".format(self.top))

    def is_empty(self):
        return self.num_items == 0  # True if the stack is empty.txt, false otherwise

    def push(self, item):
        temp = Node(item, self.top)
        self.top = temp
        self.num_items += 1

    def pop(self):
        if self.is_empty():  # stack is empty.txt
            raise IndexError(f'Index Error')
        else:  # if stack isn't empty.txt, pops item from stack and returns item
            temp = self.top.value
            self.num_items -= 1
            return temp

    def peek(self):
        if self.is_empty():  # stack is empty.txt
            raise IndexError(f'Index Error')
        else:  # returns next item to be popped
            return self.top.value

    def size(self):  # returns number of items currently in stack
        return self.num_items

    
if __name__ == "__main__":
    """    stack1 = Stack()
    print(stack1.is_empty())
    print(stack1)
    stack1.push(1)
    stack1.push(2)
    print(stack1)
    stack1.push(3)
    stack1.push(4)
    print(stack1)
    stack2 = Stack(stack1.top)
    print(stack1 == stack2)
    stack2.push(3)
    print(stack1 == stack2) """
    stack1 = Stack()
    print(stack1)
    stack1.push(6)
    stack1.push(4)
    stack1.push(2)
    stack1.push(1)
    stack1.push(3)
    stack1.push(5)
    print(stack1)
    print(stack1.peek())