import random
word_list = [
    'code',
    'institute',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent',
    'market',
    'knock',
    'blue',
    'windy',
    'coin',
    'throw',
    'silence',
    'bluff',
    'red',
    'climb',
    'rooster',
    'weaver',
    'snob',
    'kickoff',
    'match',
    'quaker',
    'banksman',
    'excite',
    'remember',
    'mend',
    'brick',
    'pruning',
    'coat',
    'emerald',
    'paraguay',
    'manic',
    'multiple',
    'square',
    'funded',
    'gross',
    'orange',
    'dream',
    'peanut',
    'strict',
    'mystic',
    'lend',
    'guide',
    'strain']


# code for selecting a word at random
def get_word():
    word = random.choice(word_list)
    return word.upper()

# code for playing the game and displaying rules
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    intro =    """
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-------
    *                                     *     |
    *                                     *     O
    *                                     *    \|/
    *        LET'S PLAY HANGMAN!!!        *     |
    *                                     *    / \\
    *                                     *
    *                                     *
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- 
    *              HOW TO PLAY            *                          
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    *  You need to guess the secret word  *
    * by choosing a letter.Each incorrect *
    *   guess brings you closer to being  *
    *   hung. Guess the right letter and  * 
    *        word and save yourself.      *  
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    """
    print(intro)
    rules = """
    You need to guess the secret word by choosing a letter.
    Each incorrect guess brings you closer to being hung.
    Guess the right letter and word and save yourself.
    Good luck!
    """
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please choose a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed the correct word! You win!")
    else:
        print("Oh no!!! The word was " + word + ". Better luck next time!")

# display of hangman stages  
def display_hangman(tries):
    stages = [  # lose:
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                  ---
                """,
                # failed 5th attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                  ---
                """,
                # failed 4th attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                  ---
                """,
                # failed 3rd attempt
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                  ---
                """,
                # failed 2nd attempt
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
                """,
                # failed 1st attempt
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                  ---
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                  ---
                """
    ]
    return stages[tries]

# running the game
def main():
    word = get_word()
    play(word)
    while input("Fancy another go? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()