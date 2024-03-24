import unittest
from queue_nodelist import *


class Testlab3(unittest.TestCase):

    def test_comprehensiveQueue(self):
        queue = Queue(2)
        with self.assertRaises(IndexError):
            queue.dequeue()
        self.assertEqual(queue.is_empty(), True)
        queue.enqueue(8)
        self.assertEqual(queue.numb_in_queue(), 1)
        queue.enqueue(3)
        with self.assertRaises(IndexError):
            queue.enqueue(3)
        self.assertEqual(queue.is_full(), True)
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(queue.dequeue(), 8)


if __name__ == '__main__':
    unittest.main()