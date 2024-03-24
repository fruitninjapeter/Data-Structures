import unittest
from concordance import *


class TestList(unittest.TestCase):

    def test_load_stop_table(self):
        a = Concordance()
        self.assertEqual(len(a.load_stop_table("stop_words.txt")), 119)  # count all 119 words
        self.assertEqual(a.load_stop_table("stop_words.txt"),
                         ['only', 'off', 'your', 'had', 'would', 'yet', 'me', 'there', 'has', 'should', 'were', 'am',
                          'an', 'my', 'might', 'its', 'as', 'at', 'these', 'rather', 'however', 'no', 'be', 'from',
                          'just', 'for', 'cannot', 'said', 'wants', 'she', 'how', 'by', 'of', 'a', 'across', 'them',
                          'then', 'i', 'our', 'or', 'nor', 'not', 'on', 'who', 'they', 'what', 'does', 'why', 'with',
                          'too', 'neither', 'do', 'their', 'about', 'all', 'hers', 'among', 'her', 'whom', 'own',
                          'could', 'let', 'while', 'most', 'can', 'and', 'must', 'says', 'least', 'also', 'other', 'so',
                          'twas', 'any', 'this', 'when', 'been', 'because', 'have', 'ever', 'but', 'else', 'did',
                          'some', 'he', 'may', 'to', 'will', 'often', 'say', 'got', 'him', 'was', 'the', 'his', 'which',
                          'if', 'us', 'after', 'either', 'in', 'is', 'it', 'tis', 'every', 'are', 'able', 'almost',
                          'we', 'you', 'dear', 'get', 'into', 'where', 'than', 'since', 'that', 'like', 'likely'])

    def test_empty_file(self):
        a = Concordance()
        with self.assertRaises(FileNotFoundError):
            a.load_stop_table("nonefile.txt")
        with self.assertRaises(FileNotFoundError):
            a.load_concordance_table(None)

    def test_concordance_file1(self):
        b = Concordance()
        b.load_stop_table("stop_words.txt")
        b.load_concordance_table("file1.txt")
        b.write_concordance("file1_test.txt")
        self.assertTrue(compare_files("file1_test.txt", "file1_sol.txt"))

    def test_concordance_file2(self):
        c = Concordance()
        c.load_stop_table("stop_words.txt")
        c.load_concordance_table("file2.txt")
        c.write_concordance("file2_test.txt")
        self.assertTrue(compare_files("file2_test.txt", "file2_sol.txt"))

    def test_concordance_declaration(self):
        d = Concordance()
        d.load_stop_table("stop_words.txt")
        d.load_concordance_table("declaration.txt")
        d.write_concordance("declaration_test.txt")
        self.assertTrue(compare_files("declaration_test.txt", "declaration_sol.txt"))


# Compare files - takes care of CR/LF, LF issues
def compare_files(file1, file2):
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2:
                    done = True
                    match = False
    return match


if __name__ == '__main__':
    unittest.main()
