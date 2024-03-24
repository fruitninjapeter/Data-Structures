import string

def test_file(filename):
    if filename is None:  # If file does not exist, raise FileNotFoundError
        raise FileNotFoundError
    with open(filename, "r") as filename:  # Read words from input file (filename)
        lines = filename.readlines()  # returns a list containing each line in file as an element
    for line in lines:  # iterate through all lines of filename
        #linecount = 1
        line = line.replace("-", " ")  # hyphen's replaced by space
        line = line.replace("'", "")  # apostrophes removed
        line = line.translate(str.maketrans('', '', string.punctuation))  # other punctuation is GONE
        line = line.translate(str.maketrans('', '', string.digits))  # all numbers are GONE
        line = line.lower()
        #line = line + " "
        print(line)
        # # # good up to here
        words = []
        word = ''
        for ch in line:  # iterate through all characters in a line
            if ch in string.ascii_lowercase:  # take care of spaces
                word += ch  # fix: we still need last word of each line
            else:
                words.append(word.rstrip())
                word = ''
        new_words = list(set(words))  # removing duplicate words, just one entry for each line number word is in
        print(new_words)



test_file("declaration2.txt")