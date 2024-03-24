import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_in_table(self):
        s = HashTable(191)
        s.insert("Doggo")
        s.insert("Peep", [90])
        s.insert("Dod")
        s.insert("Frick", 22)
        print(s.in_table("Doggo"))

    def test_get_value(self):
        s = HashTable(191)
        s.insert("Pokemon", 30)
        self.assertEqual(s.get_value("Pokemon"), 30)
        s.insert("Pokemon")  # inserting just a key with no value
        self.assertEqual(s.get_value("Pokemon"), None)
        self.assertEqual(s.get_value("doggo"), None)
        s.insert("jesus", [50, 40, 30, 20])
        self.assertEqual(s.get_value("jesus"), [50, 40, 30, 20])    # values containing lists for concordance tables
        s.insert("jesus", "Your mother lmao")   # replacing value of key
        self.assertEqual(s.get_value("jesus"), "Your mother lmao")

    def test_get_index(self):
        s = HashTable(191)
        s.insert("Pokemon", 30)
        self.assertEqual(s.get_index("Pokemon"), 110)
        self.assertEqual(s.get_index("Poopoo"), None)

    def test_num_items_and_get_all_keys(self):
        s = HashTable(191)
        self.assertEqual(s.num_items, 0)
        s.insert("Booba")
        s.insert("Boba")
        s.insert("Boob")
        self.assertEqual(s.num_items, 3)
        s.insert("ooba")
        s.insert("Booa")
        s.insert("Booba", [3, 2, 5, 0])  # duplicate item, replace key
        self.assertEqual(s.num_items, 5)
        self.assertEqual(s.get_all_keys(), ['Boba', 'Booa', 'Boob', 'Booba', 'ooba'])

    def test_in_table_and_table_size(self):
        s = HashTable(30)
        self.assertEqual(s.get_table_size(), 30)
        s = HashTable(15)   # overwrite table size
        self.assertEqual(s.get_table_size(), 15)
        s.insert("Pokemon", 69)
        self.assertTrue(s.in_table('Pokemon'))
        self.assertFalse(s.in_table("Fake News"))
        self.assertFalse(s.in_table('topology'))

    def test_load_factor_and_increase_size_and_quadratic_probe(self):
        s = HashTable(8)
        s.insert("Poop", [100, 400, 23])    # item 1
        s.insert("Popo", [9, 0, 10])    # item 2
        s.insert("popon", "Dinner Warrior")   # item 3: we have a duplicate hash index and need to probe
        self.assertEqual(s.num_items, 3)
        self.assertEqual(s.get_all_keys(), ['Poop', 'popon', 'Popo'])
        self.assertEqual(s.get_load_factor(), 3/8)
        self.assertEqual(s.get_value("popon"), "Dinner Warrior")
        # test if quadratic probe can also replace value of duplicate key
        s.insert("popon", [100])
        self.assertEqual(s.get_value("popon"), [100])
        # Now we see if increasing load factor and resizing function works
        s.insert("yeehaw")  # item 4
        self.assertEqual(s.get_load_factor(), .5)
        # item 5 sets load factor > .5: Hash Table resized, all elements rearranged
        s.insert("ride high", ["mustang"])   # item 5
        self.assertEqual(s.get_table_size(), 17)    # previous size: 8, now it's ( 8 * 2 ) + 1 = 17
        self.assertEqual(s.get_num_items(), 5)
        self.assertEqual(s.get_load_factor(), 5/17)
        self.assertEqual(s.get_value("ride high"), ["mustang"])
        # after the size increase and rearrangement, can we replace value of quadratically probed duplicate key
        s.insert("ride high", "poo")
        self.assertEqual(s.get_value("ride high"), "poo")
        s.insert("popon", [42])
        self.assertEqual(s.get_value("popon"), [42])
        self.assertEqual(s.get_all_keys(), ['ride high', 'yeehaw', 'Popo', 'popon', 'Poop'])
