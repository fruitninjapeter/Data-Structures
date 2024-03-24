class Queue:
    def __init__(self, capacity):
        self.capacity = capacity  # the maximum number of items that can be stored in queue
        self.num_in_queue = 0  # the number of items stored in queue
        self.front = 0
        self.rear = 0
        self.values = [None] * capacity

    def __eq__(self, other):
        return ((type(other) == Queue)
            and self.capacity == other.capacity
            and self.num_in_queue == other.num_in_queue
            and self.front == other.front
            and self.rear == other.rear
            and self.values == other.values)

    def __repr__(self):
        return "Queue({!r}, {!r}, {!r}, {!r}, {!r})".format(self.capacity, self.num_in_queue, self.front,
                                                            self.rear, self.values)

    def is_empty(self):  # returns a boolean for if circular queue is empty.txt
        return self.num_in_queue == 0

    def is_full(self):  # returns a boolean for if circular array is full
        return self.num_in_queue == self.capacity

    def enqueue(self, item):
        if self.is_full():  # if queue is full raise IndexError
            raise IndexError
        self.values[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity  # increment the front pointer
        self.num_in_queue += 1

    def dequeue(self):
        if self.is_empty():  # if queue is empty.txt raise IndexError
            raise IndexError
        data = self.values[self.rear]
        self.values[self.front] = None
        self.front = (self.front + 1) % self.capacity  # increment the rear pointer
        self.num_in_queue -= 1  # increment head
        return data

    def numb_in_queue(self):  # it's name change because test didn't register, returns the number of items in the queue
        if self.rear >= self.front:
            queueSize = self.rear - self.front
        else:
            queueSize = self.capacity - (self.front - self.rear)
        return queueSize    # return the size of the queue
