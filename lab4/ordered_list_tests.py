import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_OrderedList(self):
        list = OrderedList()
        self.assertEqual(list.is_empty(), True)  # test for is_empty()
        list.add(3)
        list.add(7)
        list.add(2)
        self.assertEqual(list.size(), 3)   # test for size()
        self.assertEqual(list.index(7), 2)  # tests for index()
        self.assertEqual(list.index(2), 0)
        self.assertEqual(list.index(1), -1)  # index of number not in list
        self.assertEqual(list.search_forward(2), True)  # test for search_forward()
        list.add(100)
        self.assertEqual(list.search_forward(100), True)
        self.assertEqual(list.search_forward(99), False)  # 99 isn't in list
        self.assertEqual(list.search_backward(2), True)  # test for search_backward
        self.assertEqual(list.search_forward(911), False)
        self.assertEqual(list.remove(3), 1)  # test for remove
        self.assertEqual(list.search_forward(3), False)
        self.assertEqual(list.remove(5), -1)
        self.assertEqual(list.pop(), 100)
        self.assertEqual(list.search_backward(100), False)
        list.add(100)
        self.assertEqual(list.search_backward(100), True)  # New list [2,7,100]
        list.add(5)
        self.assertEqual(list.search_forward(5), True)
        list.add(6)
        self.assertEqual(list.search_forward(6), True)


if __name__ == '__main__':
    unittest.main()