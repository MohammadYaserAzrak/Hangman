# Imported modules
import random
import string
import sys


# Functions defined
def get_valid_guess(chosen_letters, allowed_mistakes):
    while True:
        guess = input("Guess your letter: ").strip().upper()
        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("Invalid input. Please enter a single letter.")
        elif guess in chosen_letters:
            print("Letter was already chosen. Please guess again.")
        elif guess not in manipulated_correct_word:
            allowed_mistakes -= 1
            if allowed_mistakes == 0:
                sys.exit(f"You lost! The word was {CORRECT_WORD}")
            print(f"Wrong letter! You have {allowed_mistakes} tries left")
            chosen_letters.append(guess)
        else:
            return guess, allowed_mistakes, chosen_letters


def get_random_word():
    with open("random_words.txt", "r") as f:
        lines = f.readlines()
        MAX = len(lines)
        random_word_index = random.randint(0, MAX)
        return lines[random_word_index].strip()


# Main
if __name__ == "__main__":
    print("Welcome to Hangman!")
    CORRECT_WORD = get_random_word()
    manipulated_correct_word = CORRECT_WORD
    guessed_word = "_" * len(manipulated_correct_word)
    manipulated_correct_word = list(manipulated_correct_word)
    guessed_word = list(guessed_word)
    chosen_letters = []
    allowed_mistakes = 6
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
            print("You won!")
            break
