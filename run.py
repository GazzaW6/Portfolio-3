# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words_list

def get_word():
    word = random.choice(words_list)
    return word.upper()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    gussed-words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")