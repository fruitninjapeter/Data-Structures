import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_invalid(self):
        self.assertFalse(postfix_valid(""))
        self.assertFalse(postfix_valid("2 3"))
        self.assertFalse(postfix_valid("2 3 8 1 3"))

    def test_valid(self):
        self.assertTrue(postfix_valid("2 3 +"))
        self.assertTrue(postfix_valid("2 3 -"))
        self.assertTrue(postfix_valid("2 3 *"))
        self.assertTrue(postfix_valid("6 3 2 + *"))

    def test_postfixeval1(self):    # test for each operand
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("3 2 -"), 1)
        self.assertAlmostEqual(postfix_eval("8 5 *"), 40)
        self.assertAlmostEqual(postfix_eval("5 3 ^"), 125)
        self.assertAlmostEqual(postfix_eval("8 2 /"), 4)

    def test_postfixeval2(self):
        self.assertAlmostEqual(postfix_eval("6 3 2 + *"), 30)
        self.assertAlmostEqual(postfix_eval("6 3 - 2 +"), 5)

    def test_inToPostBasicAssoc1(self):  # works
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")

    def test_inToPostBasicAssoc2(self):
        self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 2 + -")

    def test_inToPostBasicAssoc3(self):  # works
        self.assertEqual(infix_to_postfix("6 ^ 3 ^ 2"), "6 3 2 ^ ^")

    def test_inToPostBasicAssoc4(self):  # works
        self.assertEqual(infix_to_postfix("6 * ( 3 + 2 )"), "6 3 2 + *")

    def test_inToPostBasicAssoc5(self):  # works
        self.assertEqual(infix_to_postfix("6"), "6")
        with self.assertRaises(ValueError):
            postfix_eval("3 0 /")


if __name__ == "__main__":
    unittest.main()