"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 9: Case Study: Word Play in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def uses_all(word, required):
    """
        Determine if a word has only the required letters

        word: string
        acceptable: string

        return: boolean, True if word contains all of the required letters; false otherwise
    """
    # set variables
    for letter in required:
        if letter not in word:
            return False
    return True
    

def user_input():
    """
        Request user input for required letters

        return: string
    """
    print("Welcome! Let's check to see if the 'words.txt' file has words with acceptable letters.\n")
    return input("Please enter your acceptable letters: ")
    

def number_of_words(required):
    """
        Open the file words.txt, count the number of words that contain the acceptable letters
    """
    # Open the file
    fin = open('words.txt')

    # set variables to 0
    i = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, required):
            i += 1
    
    # Close the file
    fin.close()

    # Print the results
    print("There are " + str(i) + " word(s) that use all the letters: " + required + ".")

number_of_words(user_input())