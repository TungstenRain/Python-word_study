"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 9: Case Study: Word Play in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.9.0
"""
def print_words():
    """
        Open the file words.txt and print the words with more than 20 characters
    """
    # Open the file
    fin = open('words.txt')
    
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)
    
    # Close the file
    fin.close()

print_words()