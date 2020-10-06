"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 9: Case Study: Word Play in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def avoids(word, forbidden):
    """
        Determine if a word has forbidden letters

        word: string
        forbidden: string

        return: boolean, True if word does not contain forbidden letters; false otherwise
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True

def user_input():
    """
        Request user input for forbidden letters

        return: string
    """
    print("Welcome! Let's check to see if the 'words.txt' file has words with forbidden letters.\n")
    return input("Please enter your forbidden letters: ")
    

def number_of_words(forbidden):
    """
        Open the file words.txt, count the number of words that do not contain the forbidden letters
    """
    # Open the file
    fin = open('words.txt')

    # set variables to 0
    i = 0
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden):
            i += 1
    
    # Close the file
    fin.close()

    # Print the results
    print("There are " + str(i) + " words that do not contain the forbidden letters: " + forbidden + ".")

number_of_words(user_input())