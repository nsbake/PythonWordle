# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    word = random.choice(FIVE_LETTER_WORDS) #this picks a random word from the WordleDictionary
    #lst= []    #make a list to store the individual letters of the word
    gw = WordleGWindow()
    #print(word)
    #print(lst)
    
    r=6 #num rows
    c=5 #num cols
    for letter in word:    #for loop to split the letters out and put into the square letter method
        #lst.append(letter)

        gw.set_square_letter(N_ROWS-r, N_COLS-c, letter)
        c -=1
    
    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    wordle()