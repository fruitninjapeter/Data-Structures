class HuffmanNode:
    def __init__(self, char_ascii, freq):
        self.char_ascii = char_ascii  # stored as an integer - the ASCII character code value
        self.freq = freq              # the frequency count associated with the node
        self.left = None              # Huffman tree (node) to the left
        self.right = None             # Huffman tree (node) to the right

    def __lt__(self, other):
        return comes_before(self, other)  # Allows use of Python List sorting

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

def comes_before(a, b):  # Returns True if node a comes before node b, False otherwise
    if a.freq == b.freq:
        return a.char_ascii < b.char_ascii
    return a.freq < b.freq  # This function helps sort a list of Huffman nodes

def combine(a, b):  # Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    if a.char_ascii < b.char_ascii:  # The new node's char value will be the lesser of the a and b char ASCII values
        charval = a.char_ascii
    else:
        charval = b.char_ascii
    parent = HuffmanNode(charval, a.freq + b.freq)  # New frequency value will be the sum of the a and b frequencies
    parent.set_left(a)
    parent.set_right(b)
    return parent

def cnt_freq(filename):  # Given file name passed as a string
    file = open(filename, 'r')  # opens the file for reading
    stuff = file.read()  # returns file to do a for loop on
    unicode_list = [0] * 256    # Python List with 256 entries - counts are initialized to zero.
    for ch in stuff:    # counts the frequency of occurrences of all the characters within that file
        i = ord(ch)  # ASCII value of the character
        unicode_list[i] += 1
    return unicode_list

def create_huff_tree(freq_list):    # Input is the list of frequencies (provided by cnt_freq()).
    if freq_list == [0] * 256:  # Returns None if all counts are zero.
        return None
    nodelist = []
    ascii = 0
    for frequency in freq_list:  # Create a Huffman tree for characters with non-zero frequency
        ascii += 1
        if frequency != 0:
            nodelist.append(HuffmanNode(ascii - 1, frequency))
    sortedlist = sorted_help(nodelist)    # make a sorted list
    while len(sortedlist) != 1:
        node1 = sortedlist[0]   # minimum node 1
        node2 = sortedlist[1]   # minimum node 2
        parent = combine(node1, node2)  # combine them to make parent node
        sortedlist[0] = parent
        sortedlist.pop(1)
        sortedlist = sorted_help(sortedlist)
    return sortedlist[0]   # Returns the root node of the Huffman tree.

def sorted_help(nodelist):  # helper function for sorting Huffman Nodes, uses insertion sort
    for i in range(1, len(nodelist)):
        current = nodelist[i]   # current node
        pos = i - 1  # node previous
        while pos >= 0 and comes_before(current, nodelist[pos]):
            nodelist[pos + 1] = nodelist[pos]
            pos = pos - 1
        nodelist[pos + 1] = current
    return nodelist

def create_code(root_node):  # Returns an array (Python list) of Huffman codes.
    arraylist = [None] * 256    # For each character, use the integer ASCII representation as the index into the array
    empties = ""  # Characters that are unused should have an empty.txt string at that location
    create_code_help(root_node, empties, arraylist)
    return arraylist

def create_code_help(node, string, list):   # helper function for create_code to recursively traverse the huffman tree
    if node is None:
        return None
    if node.left is None and node.right is None:
        list[node.char_ascii] = string
    else:   # resulting Huffman code for that character stored at that location.
        create_code_help(node.left, string + "0", list)
        create_code_help(node.right, string + "1", list)

def create_header(freq_list):   # Input is the list of frequencies (provided by cnt_freq()).
    # Creates and returns a header for the output file
    String = ""
    ascii = -1
    for i in freq_list:  # "aaabbbbcc", would return "97 3 98 4 99 2"
        ascii += 1
        if i != 0:
            String += str(ascii) + " " + str(i) + " "
    return String.rstrip()  # we have rstrip to remove whitespace at end

def huffman_encode(in_file, out_file):  # Takes inout file name and output file name as parameters
    # Uses the Huffman coding process on the text from the input file
    frequencylist = cnt_freq(in_file)   # initialize frequency list of characters for in_file
    huffman_tree = create_huff_tree(frequencylist)  # create huffman tree using said lists
    huffcodelist = create_code(huffman_tree)    # create huffman codes list using the root node
    header = create_header(frequencylist)
    with open(in_file, "r") as in_file:
        lines = in_file.readlines()
    with open(out_file, "w") as out_file:   # writes encoded text to output file
        out_file.write(header + "\n")   # First line in file is header then declare new line
        for line in lines:  # for loop for all lines of in_file
            for char in line:   # for loop for all characters in each line of in_file
                out_file.write(huffcodelist[ord(char)])
