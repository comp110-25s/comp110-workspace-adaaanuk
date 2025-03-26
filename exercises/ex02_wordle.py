"""Wordle inspiration with secret word that can accept words of multiple lengths"""

__author__: str = "730649282"


def contains_char(any_word: str, single_char: str) -> bool:
    """Tests whether a single character is located in the guessed word of any length"""
    assert len(single_char) == 1, f"len('{single_char}') is not 1"
    idx: int = 0
    while idx < len(any_word):
        if single_char == any_word[idx]:
            return True
        else:
            idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Tells user the location and correctness of characters in guess vs. secret"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    result: str = ""
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result = result + GREEN_BOX
        else:
            if contains_char(secret, guess[idx]):
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        idx += 1
    return result


def input_guess(number: int) -> str:
    """Takes a user input and prompts to ensure guess is proper length"""
    guess: str = input(f"Enter a {number} character word:")
    while len(guess) != number:
        guess = input(f"That wasn't {number} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    T: int = 1
    while T <= 6:
        print(f"=== Turn {T}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            return print(f"You won in {T}/6 turns!")
        T += 1
    return print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
