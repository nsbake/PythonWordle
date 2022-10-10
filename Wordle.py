# File: Wordle.py
"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import *

def countInWord(str, char):
    counter = 0
    for letter in str:
        if letter == char:
            counter += 1
    return counter

def wordle():
    word = random.choice(FIVE_LETTER_WORDS).upper() #this picks a random word from the WordleDictionary
    # word = 'GLASS' # test against "sassy"
    gw = WordleGWindow()
    r = N_ROWS #num rows
    c = N_COLS #num cols
    
    for letter in word:    #for loop to split the letters out and put into the square letter method
        gw.set_square_letter(N_ROWS-r, N_COLS-c, letter)
        c -=1
    
    currentRow = 1
    gw.set_current_row(currentRow)

    def enter_action(guess):
        nonlocal currentRow
        greenIdxs = [] #index of correctly placed letters

        # check invalid guess
        if guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
            gw.set_current_row(currentRow)
            return

        # check win condition
        if guess == word.upper():
            for col in range(len(guess)):
                gw.set_square_color(currentRow, col, CORRECT_COLOR)
                gw.set_key_color(gw.get_square_letter(currentRow, col), CORRECT_COLOR) 
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
            gw._enter_listeners.remove(enter_action)
            return

        # check loss condition
        if guess.lower() in FIVE_LETTER_WORDS and currentRow == 5:
            gw.show_message("Sorry! Better luck next time!")
            return # ends the whole function

        # check gameplay (non-loss, non-win, valid input)
        # find the greens first
        for col in range(len(guess)):
            currentLetter = gw.get_square_letter(currentRow, col)
            answerLetter = gw.get_square_letter(0, col)
            if currentLetter == answerLetter:
                gw.set_square_color(currentRow, col, CORRECT_COLOR)
                gw.set_key_color(currentLetter, CORRECT_COLOR) # <-- ETHAN'S MILESTONE #4: Color the keys green
                greenIdxs.append(col)
                continue # ends loop execution, then goes to the top of the loop

        letterMatches = {}
        for col in range(len(guess)):
            currentLetter = gw.get_square_letter(currentRow, col)
            letterMatches[currentLetter] = word.upper().count(currentLetter)

        # decrement if a green exists
        for greenIdx in greenIdxs:
            greenLetter = gw.get_square_letter(currentRow, greenIdx)
            letterMatches[greenLetter] -= 1

        for col in range(len(guess)):
            if col in greenIdxs: 
                continue

            currentLetter = gw.get_square_letter(currentRow, col)
            answerLetter = gw.get_square_letter(0, col)
            if currentLetter in word and letterMatches[currentLetter] > 0:
                gw.set_square_color(currentRow, col, PRESENT_COLOR)
                if gw.get_key_color(currentLetter) != CORRECT_COLOR:
                    gw.set_key_color(currentLetter, PRESENT_COLOR) 
                letterMatches[currentLetter] -= 1

            else:
                gw.set_square_color(currentRow, col, MISSING_COLOR)
                if gw.get_key_color(currentLetter) != CORRECT_COLOR and gw.get_key_color(currentLetter) != PRESENT_COLOR:
                    gw.set_key_color(currentLetter, MISSING_COLOR) 

        currentRow += 1
        gw.show_message("Good guess, try again")
        gw.set_current_row(currentRow)
            

    #callback function for enter
    gw.add_enter_listener(enter_action)

# Startup code
if __name__ == "__main__":
    try:
        wordle()
    except Exception as err:
        print(err)
        raise