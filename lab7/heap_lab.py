class MaxHeap:
    def __init__(self, capacity=50):
        self.heap = [None] * (capacity + 1)  # index 0 not used for heap
        self.num_items = 0  # empty.txt heap

    def enqueue(self, item):    # inserts "item" into the heap
        if self.is_full():  # Returns False if there is no room in the heap
            return False
        self.heap[self.num_items + 1] = item    # if we have n items, the array for each item is n + 1
        self.num_items += 1
        self.perc_up(self.num_items)
        return True

    def peek(self):  # returns max without changing the heap
        if self.is_empty():  # Raises IndexError if the heap is empty.txt"""
            raise IndexError
        return self.heap[1]  # element 1 always has the maximum

    def dequeue(self):  # returns max at root (highest priority), removes from the heap and restores the heap property
        if self.is_empty():  # Raises IndexError if the heap is empty.txt
            raise IndexError
        data = self.heap[1]  # Save max in data
        self.heap[1] = self.heap[self.num_items]    # remove and replace root element with last element in heap
        self.num_items -= 1
        self.perc_down(1)
        return data

    def contents(self):  # returns a list of contents of the heap in the order it is stored internal to the heap.
        if self.is_empty():  # If heap is empty.txt, returns empty.txt list []"""
            return []
        return self.heap[1:self.num_items+1]

    def build_heap(self, alist):  # Discards current heap items, builds heap from items in alist (bottom up method)
        i = len(alist) // 2
        self.num_items = len(alist)
        if len(self.heap) < len(alist):    # changes capacity if current heap is less than number of items in alist
            self.heap = [0] + alist[:]
        else:   # doesn't change capacity if current heap is more than number of items in alist
            self.heap[1:len(alist)+1] = alist
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def is_empty(self):  # returns True if the heap is empty.txt, false otherwise
        return self.num_items == 0

    def is_full(self):  # returns True if the heap is full, false otherwise
        return self.num_items == self.capacity()

    def capacity(self):  # Maximum entries the heap can hold: 1 less than the number of entries heap array can hold
        return len(self.heap)-1

    def size(self):  # size of the current heap
        return self.num_items

    def perc_down(self, i):  # i is an index in the heap, perc_down moves element stored
            # at that location to its proper place in the heap rearranging elements as it goes.
        while (i * 2) <= self.num_items:    # if the element's left child index is under number items we're good
            biggerchild = self.max_child(i)
            if self.heap[i] < self.heap[biggerchild]:  # if child is bigger than parent
                temp = self.heap[i]
                self.heap[i] = self.heap[biggerchild]
                self.heap[biggerchild] = temp
            i = biggerchild

    def max_child(self, i):  # checking for which child is bigger and returns the index
        if i * 2 + 1 > self.num_items:  # if there is no right child
            return i * 2
        else:
            if self.heap[i * 2] > self.heap[i * 2 + 1]:  # left child is greater than right child
                return i * 2
            else:   # right child is greater than left child
                return i * 2 + 1

    def perc_up(self, i):   # i is an index in the heap, perc_up moves element stored
        # at that location to its proper place in the heap rearranging elements as it goes
        while i // 2 > 0:   # if the parent index is not the root index
            if self.heap[i] > self.heap[i//2]:  # if the parent element is less than the child element
                temp = self.heap[i//2]  # store parent element in temp
                self.heap[i//2] = self.heap[i]  # replace parent element with child element
                self.heap[i] = temp  # former parent element is now child, they're switched!
            i = i // 2  # move up the heap

    def heap_sort_ascending(self, alist):   # perform heap sort on input alist in ascending order
        self.build_heap(alist)  # Discard the current contents of the heap, build new heap using alist items
        blist = [0] * len(alist)
        for i in range(1, len(alist)+1):   # Mutate alist to put the items in ascending order
            blist[len(alist) - i] = self.dequeue()
        return blist
