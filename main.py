# Level 06/07 Assignment: Wordle

# Computer will select a secret five-letter word. The player gets six attempts to guess the word

# After each guess, display feedback for every letter:
#   G (green) means the letter is correct and in the correct position
#   Y (yellow) means the letter is correct but in the wrong position
#   - means the letter does not appear in the word

# Import functions from wordle_functions.py

from wordle_functions import (
    choose_word,
    display_guess,
    get_guess,
    has_won,
    previous_guesses,
)

play_again = True
while play_again:
    secret_word = choose_word()
    previous_guesses.clear()

    print("Welcome to Mystery Wordle!")
    print()
    print("Guess the five-letter word.")
    print()

    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter not in word")
    print()

    attempt = 0
    won = False
    while attempt < 6:
        print(f"Attempt {attempt + 1} of 6")

        guess = get_guess()
        if guess is False:
            continue

        display_guess(guess, secret_word)
        attempt += 1

        if has_won(guess, secret_word):
            print("Congratulations! You solved the puzzle.")
            won = True
            break

    if not won:
        print(f"Sorry, you did not guess the word. The secret word was: {secret_word.upper()}")

    while True:
        answer = input("Would you like to play again? (yes/no or y/n) ").strip().lower()
        if answer == "yes" or answer == "y":
            break
        if answer == "no" or answer == "n":
            play_again = False
            break
        print("Please enter yes or no.")

print("Thanks for playing!")