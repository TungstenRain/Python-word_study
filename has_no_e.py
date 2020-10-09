"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 9: Case Study: Word Play in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def has_no_e(word):
    """
        Determine if a word has the letter 'e'

        word: string

        return: boolean, True if no 'e'; False otherwise
    """
    for letter in word:
        if letter == 'e':
            return False
    return True
    

def find_words_without_e():
    """
        Open the file words.txt, print the words without e, and compute the percentage of words in the list without "e"
    """
    # Open the file
    fin = open('words.txt')

    # set variables to 0
    i = 0
    j = 0
    for line in fin:
        word = line.strip()
        if has_no_e(word):
            print(word)
            j += 1
        i += 1
    percentage = (j / i) * 100
    print("There are " + str(i) + " words in the file. " + str(j) + " words don't have the letter 'e' in it.\nThe percentage of words in words.txt that have no 'e' is: " + str(round(percentage, 3)) + "%.")
    
    # Close the file
    fin.close()

find_words_without_e()