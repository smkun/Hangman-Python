import random
import os
import time

from Hangman_words import word_list  # Ensure this module exists
from Hangman_art import logo, stages  # Ensure this module exists

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # for Windows
        _ = os.system('cls')
    else:  # for Linux and Mac
        _ = os.system('clear')

def play_hangman():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6
    guessed_letters = []

    print(logo)
    display = ["_"] * word_length
    print(f"{' '.join(display)}")  # Show the blanks at the start

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Input validation for guesses
        while not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
            if guess in guessed_letters:
                print(f"You've already guessed {guess}.")
            else:
                print("Please, enter a single letter.")
            guess = input("Guess a letter: ").lower()
        
        guessed_letters.append(guess)
        clear_screen()

        print(f"Letters already guessed: {', '.join(guessed_letters)}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"{guess} is not in the word, you lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word was {chosen_word}.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])

    # Input validation for playing again
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    while play_again not in ['y', 'n']:
        print("Please, enter 'y' for yes or 'n' for no.")
        play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        
    if play_again == "y":
        clear_screen()
        play_hangman()
    else:
        print("Thank you for playing!! Have a great day!!")
        time.sleep(2)

play_hangman()
