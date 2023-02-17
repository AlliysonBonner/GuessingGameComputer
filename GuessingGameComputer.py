import random

def computer_guess(highest_number: int) -> None:
    """Starts the guessing game where the computer must guess the user's secret number.

    Args:
        highest_number (int): The highest possible number that can be guessed.
    """
    # Set the initial guessing range for the computer.
    low = 1
    high = highest_number
    feedback = ''  # Initialize feedback to an empty string.

    # Keep guessing until the computer gets the correct number.
    while feedback != 'c':
        if low != high:
            # If the current range has more than one number, choose a random number.
            guess = random.randint(low, high)
        else:
            # If the current range has only one number, choose that number.
            guess = low

        # Get user feedback on the computer's guess.
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?: ').lower()

        # Modify the computer's guessing range based on the user feedback.
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    # Print a message when the computer guesses the correct number.
    print(f'The computer guessed your number, {guess}, correctly!')

if __name__ == "__main__":
    print("Welcome to the guessing game")

    # Prompt user to choose the highest possible secret number.
    highest_number = 0
    while highest_number <= 1:
        highest_number = int(input("What's the highest possible secret number in this game: "))

    # Start the guessing game.
    computer_guess(highest_number)
