from hash_quad import *
import string

class Concordance:
    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        if filename is None:    # If file does not exist, raise FileNotFoundError
            raise FileNotFoundError
        self.stop_table = HashTable(191)    # Starting size of hash table should be 191
        with open(filename, "r") as filename:   # Read stop words from input file (filename)
            lines = filename.readlines()
        for line in lines:  # iterate through all lines of filename
            self.stop_table.insert(line.strip('\n'))    # insert each word as a key into the stop words hash table.
        return self.stop_table.get_all_keys()

    def load_concordance_table(self, filename):
        if filename is None:  # If file does not exist, raise FileNotFoundError
            raise FileNotFoundError
        self.concordance_table = HashTable(191)  # Starting size of hash table should be 191
        with open(filename, "r") as filename:  # Read words from input file (filename)
            lines = filename.readlines()    # returns a list containing each line in file as an element
        linecount = 1
        for line in lines:  # iterate through all lines of filename
            line = line.replace("-", " ")  # hyphen's replaced by space
            line = line.replace("'", "")  # apostrophes removed
            line = line.translate(str.maketrans('', '', string.punctuation))    # other punctuation is GONE
            line = line.translate(str.maketrans('', '', string.digits))  # all numbers are GONE
            line = line.lower()  # capitalized letters are all lowercase
            line = line + " "   # some words are at end of line, have space so program can add to HashTable
            words = []
            word = ''
            for ch in line:  # iterate through all characters in a line
                if ch in string.ascii_lowercase:  # take care of spaces
                    word += ch
                elif word == '':  # take into account double spaces and other stuff; incomplete words
                    pass
                else:
                    words.append(word.rstrip())  #
                    word = ''
            new_words = list(set(words))  # removing duplicate words, just one entry for each line number word is in
            for i in new_words:  # Insert remaining words into the concordance hash table and lines they appear in.
                if self.stop_table.in_table(i) is False:  # Filter out words that are in the stop words hash table
                    # insert (key, value); value is a Python List with the line number
                    if self.concordance_table.in_table(i) is False:  # If word is not in table
                        self.concordance_table.insert(i, [linecount])   # insert (key, value)
                    else:   # If word is in table...
                        linelist = self.concordance_table.get_value(i)  # get current value (list of line numbers)
                        linelist.append(linecount)  # append new line number
                        self.concordance_table.insert(i, linelist)
            linecount += 1

    def write_concordance(self, filename):
        # Write the concordance entries to the output file(filename) See sample output files for format.
        entries = sorted(self.concordance_table.get_all_keys())  # sort all keys in alphabetical order
        with open(filename, "w") as filename:  # writes encoded text to filename
            for i in range(0, len(entries)):
                line_array = self.concordance_table.get_value(entries[i])
                linestring = ""
                for j in line_array:
                    linestring += " " + str(j)
                if i < len(entries) - 1:
                    filename.write(entries[i] + ":" + linestring + "\n")
                else:
                    filename.write(entries[i] + ":" + linestring)
