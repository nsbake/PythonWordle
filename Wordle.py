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
    currentRow = 1
    gw.set_current_row(currentRow)
    def enter_action(s):
        nonlocal currentRow
        #set empty string
        tempWord= ""
        for x in range(5):
            #create string of guess letters
            tempWord = tempWord + gw.get_square_letter(currentRow,x)
        #check if guess is in list
        if tempWord.upper() == word.upper():
            if currentRow == 1:
                gw.show_message("Wow! You got lucky")
            elif currentRow == 2:
                gw.show_message("Impressive!")
            elif currentRow == 3:
                gw.show_message("Great job!")
            elif currentRow == 4:
                gw.show_message("Nice job!")
            elif currentRow == 5:
                gw.show_message("That was close...")
        elif tempWord.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Good guess, try again")
            currentRow += 1
            gw.set_current_row(currentRow)
        else:
            gw.show_message("Not in word list")
            gw.set_current_row(currentRow)
    #callback function for enter
    gw.add_enter_listener(enter_action)
# Startup code
if __name__ == "__main__":
    wordle()
