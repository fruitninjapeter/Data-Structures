import string

experiment = "quicksort's  \"earthquake\"  time-consuming African-American 3.141592654"
print(experiment)
experiment = experiment.replace("-", " ")    # hyphen's replaced by space
print(experiment)
experiment = experiment.replace("'", "")    # apostrophes removed
print(experiment)
# no numbers or punctuation:
experiment = experiment.translate(str.maketrans('', '', string.punctuation))
print(experiment)
experiment = experiment.translate(str.maketrans('', '', string.digits))
experiment = experiment.lower()
print(experiment)
poop = "hello"
poop = poop.translate(str.maketrans('', '', string.punctuation))


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
        print(line)


    #with open(outfile, "w") as outfile:
    #    outfile.write(filedata)


#test_file_convert("file2.txt", "file2_zzz.txt")
