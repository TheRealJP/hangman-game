# Hangman Game
# By Juan Ortiz

import random

print('Welcome to the HANGMAN man')
print('Starting a new game...')

# RANDOMLY PICK WORD FROM FILE
words = open('hangman_words.txt').readlines()
word = random.choice(words)
guesses = ''
turns = 10

# GENERATE SCOREBOARD/WORD PROGRESS
while turns > 0:
    letters_remaining = 0
    for char in word:
        if char in guesses:
            print(char, ' ', end=''),
        else:
            print("_ ", end=''),
            letters_remaining += 1
    if letters_remaining == 0:
        print('YOU WIN!')
        break

# PLAY THE GUESSING GAME
    print()
    guess = input('Guess a letter:')
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong, try again.")
        print("You have", turns, "guesses left")
        if turns == 0:
            print('YOU LOSE')
            exit
