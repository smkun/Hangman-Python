# Hangman Game

This is a simple command-line implementation of the classic Hangman game in Python. The game randomly selects a word from a predefined list and the player must guess the word by suggesting letters within a limited number of attempts.

## How to Play

1. Run the Python script `hangman.py` in your terminal or command prompt.
2. The game will display a series of underscores representing the letters in the word to be guessed.
3. Enter a letter as your guess.
   - If the letter is in the word, it will be revealed in its correct position(s).
   - If the letter is not in the word, you will lose a life and the Hangman stage will be updated.
4. Keep guessing letters until you either guess the entire word or run out of lives.
5. If you guess the word correctly, you win the game. If you run out of lives, you lose and the correct word will be revealed.
6. After the game ends, you will be prompted to play again. Enter 'y' to play another round or 'n' to exit the game.

## Requirements

- Python 3.x
- `Hangman_words` module (contains the list of words for the game)
- `Hangman_art` module (contains the ASCII art for the game logo and Hangman stages)

Make sure the `Hangman_words.py` and `Hangman_art.py` files are in the same directory as the `hangman.py` script.

## Code Structure

The code consists of the following main components:

1. `clear_screen()` function:
   - Clears the console screen for a better user experience.
   - Uses the appropriate command based on the operating system ('cls' for Windows, 'clear' for Linux and Mac).

2. `play_hangman()` function:
   - The main game loop that handles the gameplay.
   - Selects a random word from the word list and initializes variables.
   - Prompts the user to guess letters and updates the game state accordingly.
   - Checks for win or loss conditions and displays appropriate messages.
   - Offers the option to play again after the game ends.

3. Input validation:
   - Validates user input to ensure it is a single alphabetic character and not already guessed.
   - Prompts the user to enter a valid input if the input is invalid.

4. Game flow:
   - The game starts by displaying the game logo and the initial word with underscores.
   - The player is prompted to guess a letter in each iteration of the game loop.
   - If the guessed letter is in the word, it is revealed in the display.
   - If the guessed letter is not in the word, the player loses a life and the Hangman stage is updated.
   - The game ends when either the player guesses the entire word or runs out of lives.
   - The player is given the option to play again or exit the game.

## Customization

You can customize the game by modifying the following:

- `Hangman_words.py`: Add or remove words from the `word_list` to change the words used in the game.
- `Hangman_art.py`: Modify the ASCII art for the game logo and Hangman stages to personalize the game's appearance.

## Acknowledgements

This Hangman game implementation is inspired by the classic word-guessing game and is created as a fun programming exercise.

Feel free to contribute to the code, report any issues, or suggest enhancements on the GitHub repository.

Enjoy playing Hangman!