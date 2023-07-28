# Imported modules
import random
import string
import sys
from typing import Tuple
from hangman import Hangman


# Functions defined
def get_random_word():
    with open("sowpods.txt", "r") as f:
        lines = f.readlines()
        MAX = len(lines)
        random_word_index = random.randint(0, MAX)
        return lines[random_word_index].strip()


def get_valid_guess(
    chosen_letters: list, allowed_mistakes: int
) -> Tuple[str, int, list]:
    while True:
        guess = input("Guess your letter: ").strip().upper()
        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("Invalid input. Please enter a single letter.")
        elif guess in chosen_letters:
            print("Letter was already chosen. Please guess again.")
        elif guess not in manipulated_correct_word:
            allowed_mistakes -= 1
            print(f"Wrong letter! You have {allowed_mistakes} tries left")
            if allowed_mistakes == 6:
                Hangman.draw_head(hangman)
            elif allowed_mistakes == 5:
                Hangman.draw_body(hangman)
            elif allowed_mistakes == 4:
                Hangman.draw_left_arm(hangman)
            elif allowed_mistakes == 3:
                Hangman.draw_right_arm(hangman)
            elif allowed_mistakes == 2:
                Hangman.draw_body(hangman)
            elif allowed_mistakes == 1:
                Hangman.draw_left_leg(hangman)
            elif allowed_mistakes == 0:
                Hangman.draw_right_leg(hangman)
                Hangman.game_lost(hangman, CORRECT_WORD)
                temp = input("Enter any key to exit...")
                sys.exit(1)
            chosen_letters.append(guess)
        else:
            return guess, allowed_mistakes, chosen_letters


# Main
def main(manipulated_correct_word, hangman):
    guessed_word = "_" * len(manipulated_correct_word)
    manipulated_correct_word = list(manipulated_correct_word)
    guessed_word = list(guessed_word)
    chosen_letters = []
    allowed_mistakes = 7
    guess, allowed_mistakes, chosen_letters = get_valid_guess(
        chosen_letters, allowed_mistakes
    )
    while True:
        if guess in manipulated_correct_word:
            index = manipulated_correct_word.index(guess)
            guessed_word[index] = guess
            manipulated_correct_word[index] = "_"

        else:
            print("".join(guessed_word))
            chosen_letters.append(guess)
            guess, allowed_mistakes, chosen_letters = get_valid_guess(
                chosen_letters, allowed_mistakes
            )

        if "_" not in guessed_word:
            Hangman.game_won(hangman, CORRECT_WORD)
            temp = input("Enter any key to exit...")
            return


# Starting point
if __name__ == "__main__":
    print("Welcome to Hangman!")
    CORRECT_WORD = get_random_word()
    manipulated_correct_word = CORRECT_WORD
    hangman = Hangman()
    hangman.draw_gallows()
    main(manipulated_correct_word, hangman)
