"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 9: Case Study: Word Play in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def is_abecedarian(word):
    """
        Determine if a word is in alphabetical order

        word: string
        
        return: boolean
    """
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

def number_of_words():
    """
        Open the file words.txt, count the number of words that are in alphabetical order
    """
    # Open the file
    fin = open('words.txt')

    # set variables to 0
    i = 0
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            i += 1
    
    # Close the file
    fin.close()

    # Print the results
    print("There are " + str(i) + " words in alphabetical order.")

number_of_words()