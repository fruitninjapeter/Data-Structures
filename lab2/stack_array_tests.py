import unittest
from stack_array import Stack


class TestLab2(unittest.TestCase):
    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None] * 5)
        self.assertEqual(stack.capacity, 5)
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)
        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5, [1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_is_empty(self):
        stackempty = Stack(3,[])
        stacknotempty = Stack(3,[1])
        self.assertEqual(stackempty.is_empty(), True)
        self.assertEqual(stacknotempty.is_empty(), False)

    def test_isfull(self):
        stackfull = Stack(4, [69, 69, 69, 69])
        stacknotfull = Stack(2, [1])
        self.assertEqual(stackfull.is_full(), True)
        self.assertEqual(stacknotfull.is_full(), False)

    def test_push(self):
        stack = Stack(5, [1, 2])
        stack.push(4)
        self.assertEqual(stack, Stack(5, [1, 2, 4]))

    def test_pusherror(self):
        stack = Stack(1, [3])
        with self.assertRaises(IndexError):
            stack.push(3)

    def test_pop(self):
        liststack = [5,-2,-9]
        stack = Stack(3, liststack)
        stack.pop()  # -9
        self.assertEqual(stack.pop(), -2)  # pops again-
        self.assertEqual(stack, Stack(3, [5]))
        self.assertEqual(stack.num_items, 1)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.num_items, 0)
        self.assertEqual(stack, Stack(3))

    def test_poperror(self):
        stack = Stack(6, [])
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self):
        stack = Stack(2, [3, "ch"])
        self.assertEqual(stack.peek(), "ch")

    def test_peekerror(self):
        stack = Stack(29, [])
        with self.assertRaises(IndexError):
            stack.peek()

    def test_size(self):
        stack = Stack(7, [4, 2, 9, 1])
        self.assertEqual(stack.size(), 4)
        stack.push(3)
        stack.push(3)
        self.assertEqual(stack.size(), 6)
        self.assertEqual(stack.pop(), 3)


if __name__ == '__main__':
    unittest.main()