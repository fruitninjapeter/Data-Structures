class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return (self.data == other.data
            and self.next == other.next
            and self.prev == other.prev
            and isinstance(self, Node) == isinstance(other, Node))

    def __repr__(self):
        return "Node({!r}, {!r})".format(self.data, self.next)

    def get_data(self):
        return self.data

    def set_next(self, newnext):
        self.next = newnext

    def set_prev(self, newprev):
        self.prev = newprev


class OrderedList:  # creates a new ordered list that is empty.txt; returns an empty.txt list

    def __init__(self):
        self.head = None  # where the smallest items are
        self.tail = None  # where the largest items are
        self.num_items = 0

    def __repr__(self):
        return "OrderedList({})".format(self.head)

    def __eq__(self, other):
        return (isinstance(self, OrderedList) ==
                isinstance(other, OrderedList) and
                self.head == other.head and
                self.tail == other.tail and
                self.num_items == other.num_items)

    def add(self, item):  # adds new item to list while making sure the order is preserved
        if self.head is None:   # there are no items in the list
            self.head = Node(item)  # assign first item to be the Node head
            self.tail = self.head   # only one item in list: the Node is both head and tail
            self.head = self.tail
            self.num_items += 1  # increments number of items
        else:  # there are already items in the list
            if item > self.head.get_data():  # if the number is greater than the least number in list
                current = self.head  # starts with least number
                while current and item > current.get_data():  # progresses up until item is less than current
                    current = current.next
                if current is None:  # if we have reached the end of list
                    new = Node(item)
                    self.tail.set_next(new)
                    new.set_prev(self.tail)
                    new.set_next(None)
                    self.tail = new
                    self.num_items += 1
                else: #
                    new = Node(item)
                    next = current
                    prev = current.prev
                    prev.set_next(new)
                    next.set_prev(new)
                    new.set_next(current)
                    new.set_prev(prev)
                    self.num_items += 1
            else:  # if number is less than the least number in the list
                new_node = Node(item)
                new_node.set_prev(None)
                new_node.set_next(self.head)
                self.head.set_prev(new_node)
                self.head = new_node
                current = self.head
                while current.next:
                    current = current.next
                self.tail = current
                self.num_items += 1

    def remove(self, item):  # removes item from the list, modifies the list
        position = self.index(item)  # uses index function to find where item is
        if position == -1:
            return -1
        current = self.head
        i = 0
        while i < position:
            i += 1
            current = current.next
        previous = current.prev
        next = current.next
        previous.set_next(next)
        next.set_prev(previous)
        current = None
        self.num_items -= 1
        return position

    def search_forward(self, item):  # searches for the item in the list, needs the item and returns a boolean value
        current = self.head
        if current.get_data() == item:
            return True
        i = 0
        while i < self.size():
            i += 1
            if current.get_data() == item:
                return True
            current = current.next
        return False

    def search_backward(self, item):  # searches for the item in the list starting from the tail of list; boolean
        current = self.tail
        if current.get_data() == item:
            return True
        i = self.size()
        while i > 0:
            i -= 1
            if current.get_data() == item:
                return True
            current = current.prev
        return False

    def is_empty(self):  # tests to see whether the list is empty.txt
        return self.head is None

    def size(self):  # returns the number of items in the list
        return self.num_items

    def index(self, item):  # returns the position of item on the list, it needs the item and returns the index
        index = 0
        current = self.head
        if current.get_data() == item:
            return 0
        i = 0
        while i < self.size():
            i += 1
            if current.get_data() == item:
                return index
            current = current.next
            index += 1
        return -1

    def pop(self, pos=None):  # removes and returns Node, given position is optional
        # pop(pos) should compare pos to the size of the list and search from
        # the head if pos <= size/2 and from the rear if pos > size/2.
        if self.head is None:
            raise IndexError
        if pos is None:
            current = self.tail.get_data()
            previous = self.tail.prev
            if previous:
                previous.set_next(None)
            self.tail.set_prev(None)
            self.tail = previous
            if self.tail is None:
                self.head = None
            self.num_items -= 1
            return current
        if pos <= self.size()/2:    # search from the head if pos <= size/2
            current = self.head
            i = 0
            if i == pos:
                current = current.get_data()
                self.remove(current)
                return current
            while i <= self.size()/2:
                current = current.next
                i += 1
                if i == pos:
                    self.remove(current)
                    return current
                if current is None:
                    raise IndexError
        if pos > self.size():
            current = self.tail
            i = self.size()
            if i == pos:
                self.remove(current)
                return current
            while i > self.size()/2:
                current = current.prev
                i -= 1
                if i == pos:
                    self.remove(current)
                    return current
                if current is None:
                    raise IndexError
