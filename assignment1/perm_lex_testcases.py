# CPE 202 Assignment 1 Part 1 Test Cases
import unittest
from perm_lex import *


class TestPart1(unittest.TestCase):

    def test_nocharacter(self):
        """test for string containing no characters """
        self.assertEqual(perm_gen_lex(''), [''])

    def test_onecharacter(self):
        """test for string containing one character"""
        self.assertEqual(perm_gen_lex('a'),['a'])

    def test_twocharacter(self):
        """test for two character string"""
        self.assertEqual(perm_gen_lex('ab'),['ab', 'ba'])

    def test_threecharacter(self):
        """test for three character string"""
        self.assertEqual(perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])


if __name__ == "__main__":
        unittest.main()