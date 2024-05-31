import random
import os
import time

from Hangman_words import word_list  # Ensure this module exists
from Hangman_art import logo, stages  # Ensure this module exists

# Function to clear the screen
def clear_screen():
    """
    Clears the console screen.
    Uses 'cls' command for Windows and 'clear' command for Linux and Mac.
    """
    if os.name == 'nt':  # for Windows
        _ = os.system('cls')
    else:  # for Linux and Mac
        _ = os.system('clear')

def play_hangman():
    """
    Main function to play the Hangman game.
    Selects a random word from the word list, initializes variables,
    and starts the game loop. Handles user input, updates the game state,
    and checks for win or loss conditions. Offers the option to play again.
    """
    chosen_word = random.choice(word_list)  # Select a random word from the word list
    word_length = len(chosen_word)  # Get the length of the chosen word
    end_of_game = False  # Flag to indicate if the game has ended
    lives = 6  # Number of lives the player starts with
    guessed_letters = []  # List to store the letters guessed by the player

    print(logo)  # Display the game logo
    display = ["_"] * word_length  # Create a list of underscores to represent the hidden word
    print(f"{' '.join(display)}")  # Show the blanks at the start

    while not end_of_game:
        guess = input("Guess a letter: ").lower()  # Prompt the user to guess a letter

        # Input validation for guesses
        while not guess.isalpha() or len(guess) != 1 or guess in guessed_letters:
            if guess in guessed_letters:
                print(f"You've already guessed {guess}.")
            else:
                print("Please, enter a single letter.")
            guess = input("Guess a letter: ").lower()
        
        guessed_letters.append(guess)  # Add the guessed letter to the list of guessed letters
        clear_screen()  # Clear the screen

        print(f"Letters already guessed: {', '.join(guessed_letters)}")  # Display the letters already guessed

        # Check if the guessed letter is in the chosen word
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter  # Reveal the guessed letter in the display

        # If the guessed letter is not in the chosen word
        if guess not in chosen_word:
            print(f"{guess} is not in the word, you lose a life.")
            lives -= 1  # Decrement the number of lives
            if lives == 0:  # If the player has no more lives
                end_of_game = True  # Set the end_of_game flag to True
                print(f"You lose. The word was {chosen_word}.")  # Display the losing message and reveal the word

        print(f"{' '.join(display)}")  # Display the updated word with revealed letters

        # If there are no more underscores in the display, the player has guessed all the letters
        if "_" not in display:
            end_of_game = True  # Set the end_of_game flag to True
            print("You win.")  # Display the winning message

        print(stages[lives])  # Display the Hangman stage corresponding to the remaining lives

    # Input validation for playing again
    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    while play_again not in ['y', 'n']:
        print("Please, enter 'y' for yes or 'n' for no.")
        play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
        
    if play_again == "y":
        clear_screen()  # Clear the screen
        play_hangman()  # Restart the game by calling the play_hangman function
    else:
        print("Thank you for playing!! Have a great day!!")
        time.sleep(2)  # Pause for 2 seconds before exiting

# Run the game when the script is executed directly
if __name__ == "__main__":
    play_hangman()  # Start the game by calling the play_hangman function