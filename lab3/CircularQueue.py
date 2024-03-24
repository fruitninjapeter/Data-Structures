# This is the CircularQueue class
class CircularQueue:

    def __init__(self, maxSize):  # constructor for the class taking input for the size of the Circular queue from user
        self.queue = list()  # user input value for maxSize
        self.maxSize = maxSize
        self.head = 0
        self.tail = 0

    def enqueue(self, data):  # add element to the queue
        if self.size() == (self.maxSize - 1): # if queue is full
            return ("Queue is full!")
        else:
            self.queue.append(data) # add element to the queue
            # increment the tail pointer
            self.tail = (self.tail + 1) % self.maxSize
            return True

    def dequeue(self): # remove element from the queue
        # if queue is empty.txt
        if self.size() == 0:
            return ("Queue is empty.txt!")
        else:
            # fetch data
            data = self.queue[self.head]
            # increment head
            self.head = (self.head + 1) % self.maxSize
            return data

    def size(self):  # find the size of the queue
        if self.tail >= self.head:
            qSize = self.tail - self.head
        else:
            qSize = self.maxSize - (self.head - self.tail)
        # return the size of the queue
        return qSize


# input 7 for the size or anything else
size = input("Enter the size of the Circular Queue")
q = CircularQueue(int(size))

# change the enqueue and dequeue statements as you want
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.enqueue('Studytonight'))
print(q.enqueue(70))
print(q.enqueue(80))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())