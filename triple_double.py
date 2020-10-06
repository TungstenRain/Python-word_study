"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 9: Case Study: Word Play in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def is_triple_double(word):
    """
        Determines if a word contains three consecutive double letters

        word: string

        return: boolean
    """
    # set variables to 0
    i = 0
    count = 0
    while i < (len(word) - 1):
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i = i + 1 - (2 * count)
            count = 0
    return False

def find_triple_double():
    """
        Count the number of triple double words in 'words.txt'
    """
    # Open the file
    fin = open('words.txt')

    # Instantiate the list
    triple_double = []

    # Loop through the file
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            triple_double.append(word)
    
    # Close the file
    fin.close()

    # Print the results
    print("There are " + str(len(triple_double)) + " words with three consecutive double letters.")
    for word in triple_double:
        print(word)
    

find_triple_double()