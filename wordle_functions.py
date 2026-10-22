from random import random

# Keep a list of player's previous guesses
previous_guesses = []

def choose_word():
    # Pre-determined list of five-letter words
    # Yes, AI helped generate a bajillion of these
    word_list = [
        "grape", "poopy", "loser", "peach", "mango", "lemon", "melon", "thyme",
        "mikey", "kirby", "basil", "cumin", "tulip", "sugar", "spice", "limes",
        "apple", "berry", "grill", "plums", "guava", "olive", "onion", "bread",
        "toast", "pasta", "pizza", "cream", "honey", "candy", "chips", "brown",
        "green", "black", "white", "happy",
    ]

    # Randomly select a secret word
    secret_word = word_list[int(random() * len(word_list))]

    # Send back the secret word
    return secret_word

def get_guess():
    # Get and validate the player's guess

    player_guess = input("Enter a five-letter word: ").strip().lower()

    # Validate the guess (no fake words or 1-4, 6+ letter words. Five is right and that's that Jack)
    if len(player_guess) != 5:
        print("Guess must be a five-letter word.")
        return False
    elif not player_guess.isalpha():
        print("Guess must only contain letters.")
        return False
    elif player_guess in previous_guesses:
        print("You have already guessed that word.")
        return False

    # Add the guess to the list of previous guesses
    previous_guesses.append(player_guess)
    return list(player_guess)

def evaluate_guess(player_guess, secret_word):
    # Compares the guess with the secret word and returns feedback

    feedback = ["-"] * 5
    unmatched_letters = {}

    # Check for correct letters in the correct position (green)
    for i in range(5):
        if player_guess[i] == secret_word[i]:
            feedback[i] = "G"
        else:
            unmatched_letters[secret_word[i]] = unmatched_letters.get(secret_word[i], 0) + 1

    # Check for correct letters in the wrong position (yellow)
    for i in range(5):
        if feedback[i] == "-" and unmatched_letters.get(player_guess[i], 0) > 0:
            feedback[i] = "Y"
            unmatched_letters[player_guess[i]] -= 1

    return feedback

def display_guess(guess_word, secret_word):
    # Displays the guess and its feedback
    feedback = evaluate_guess(guess_word, secret_word)

    # Make it look nice and pretty
    print("Guess:    " + " ".join(letter.upper() for letter in guess_word))
    print("Feedback: " + " ".join(feedback))

def has_won(player_guess, secret_word):
    # Determines if the player has guessed the word correctly
    return "".join(player_guess) == secret_word