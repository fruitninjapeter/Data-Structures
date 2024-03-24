import unittest
from heap_lab import *


class TestLab7(unittest.TestCase):

    def test_empty_heap(self):
        heap = MaxHeap(50)  # creates a minimum heap with capacity 50
        self.assertEqual(heap.is_full(), False)
        self.assertEqual(heap.is_empty(), True)
        self.assertEqual(heap.contents(), [])
        with self.assertRaises(IndexError):  # there's no elements in list, so no max
            heap.peek()
        self.assertEqual(heap.size(), 0)
        self.assertEqual(heap.capacity(), 50)
        with self.assertRaises(IndexError):
            heap.dequeue()

    def test_enqueue_error(self):
        heap = MaxHeap(1)
        self.assertEqual(heap.enqueue(69), True)
        self.assertEqual(heap.enqueue(4), False)

    def test_comprehensive_heap(self):
        heap = MaxHeap(3)
        self.assertEqual(heap.enqueue(4), True)
        self.assertEqual(heap.capacity(), 3)
        self.assertEqual(heap.peek(), 4)
        self.assertEqual(heap.enqueue(8), True)
        self.assertEqual(heap.enqueue(9), True)
        self.assertEqual(heap.contents(), [9, 4, 8])
        self.assertEqual(heap.dequeue(), 9)
        self.assertEqual(heap.size(), 2)
        self.assertEqual(heap.contents(), [8, 4])
        # build heap test
        newlist = [4, 2, 12, 3, 5, 10]
        heap.build_heap(newlist)
        self.assertEqual(heap.contents(), [12, 5, 10, 3, 2, 4])
        self.assertEqual(heap.capacity(), 6)
        # build another heap + other tests
        newerlist = [2, 3, 8]
        heap.build_heap(newerlist)
        self.assertEqual(heap.contents(), [8, 3, 2])
        self.assertEqual(heap.capacity(), 6)
        self.assertEqual(heap.size(), 3)
        # heapsort test
        alist = [2, 9, 7, 6, 5, 8]  # list given in class to do heapsort
        self.assertEqual(heap.heap_sort_ascending(alist), [2, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
