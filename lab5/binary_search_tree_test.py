import unittest
from binary_search_tree import *


class TestLab5(unittest.TestCase):

    def test_empty(self):
        r = BinarySearchTree()
        self.assertTrue(r.is_empty())
        r.insert(6)
        self.assertFalse(r.is_empty())

    def test_everything(self):
        r = BinarySearchTree()
        r.insert(6)
        r.insert(5)
        r.insert(4)
        r.insert(1)
        self.assertEqual(r.find_min(), 1)
        r.insert(7)
        r.insert(10)
        r.insert(69)
        self.assertEqual(r.find_max(), 69)
        self.assertEqual(r.inorder_print_tree(), [1, 4, 5, 6, 7, 10, 69])
        r.insert(32)
        self.assertEqual(r.print_tree(), [1, 4, 5, 6, 7, 10, 32, 69])
        self.assertEqual(r.print_levels(),
                         [[1, 3], [4, 2], [5, 1], [6, 0], [7, 1], [10, 2], [32, 4], [69, 3]])
        self.assertTrue(r.find(1))
        self.assertTrue(r.find(69))
        self.assertTrue(r.find(32))
        self.assertFalse(r.find(68))
        r.delete(1)
        self.assertEqual(r.inorder_print_tree(), [4, 5, 6, 7, 10, 32, 69])
        self.assertEqual(r.print_levels(),
                         [[4, 2], [5, 1], [6, 0], [7, 1], [10, 2], [32, 4], [69, 3]])

    def test_deleteonechild(self):
        p = BinarySearchTree(5)
        p.insert(4)
        p.insert(3)
        p.insert(2)
        p.insert(1)
        self.assertEqual(p.print_levels(),
                         [[1, 4], [2, 3], [3, 2], [4, 1], [5, 0]])
        p.delete(1)
        self.assertEqual(p.print_tree(), [2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
