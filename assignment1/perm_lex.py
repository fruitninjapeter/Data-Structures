# If the string contains a single character return a list containing that string
# Loop through all character positions of the string containing the characters to be permuted, for each character
# Form a simpler string by removing the character
# Generate all permutations of the simpler string recursively
# Add the removed character to the front of each permutation of the simpler word, and
# add the resulting permutation to a list
# Return all these newly constructed permutations

def perm_gen_lex(str):
    if len(str) <= 1:  # Case where a string has 0 or 1 letters
        return [str]
    result = [] # empty.txt array for future appending
    for i, char in enumerate(str):
        removedletter = char  # consider first character (can say remove)
        left_and_right = str[:i] + str[i + 1:]  # other strings
        for j in perm_gen_lex(left_and_right): # generate all permutations of simpler string recursively
            result.append(removedletter + j)  # add first letter to string and append final string to the result
    return result


print(perm_gen_lex('abc'))