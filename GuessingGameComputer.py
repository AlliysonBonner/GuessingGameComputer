# Guessing Game - Computer agent
# The user comes up with a secret number and we can have the computer try to guess it.
# The computer takes a guess and the user gives the computer feedback. the computer 
# takes this feed back an incorperates this knowledge to help it make its next guess.

# Author: Alliyson Bonner
# Github: https://github.com/alliysonbonner
# Linkedin: https://www.linkedin.com/in/alliyson-bonner-6404976b/
# Email: alliyson.bonner@gmail.com
# Date: December 07 2022

# Import libraries
import random

def computer_guess(highest_number):
  """Starts the guess game where the computer must guess the correct
  number to win.
  Args:
      highest_number(int): This is the highest posible number that
      can be guessed.
  """
  # Set lowest number the computer can guess to 1. 
  # Set the highest number the computer can guess to highest_number.
  low = 1
  high = highest_number
  
  # Set feedback to empty string. Get guesses from the computer until
  # the guess is correct.
  feedback = ''
  while feedback != 'c':
  	# Set guess to a random number between low and high, inclusivly, 
    # if low does not equal high. Set guess to low or high if low 
    # equals high.
    if low != high:
      guess = random.randint(low, high) 
    else:
      guess = low # could also be high b/c low = high
  	
    # Prompt user to respond to the guess given by the computer with 
    # H, L, or C depending on if the computer's guess is too high,
    # too low, or correct, respectiively. If the computer guesses 
    # incorrectly, modify the computer's guessing range for the next
    # guess.
    feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?: ').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1
    
  # Give response when the computer guesees correctly.
  print(f'Whoop! Whoop! The computer guessed your number, {guess}, corrrectly!!')
    
if __name__ == "__main__":
  # Display welcome message
  print("Welcome to the guessing game")
  # Keep prompting user to choose a number until their number is higher than 1
  highest_number = 0
  while highest_number <= 1:
  	highest_number = int(input("What's the highest possible secret number in this \
game: "))
  # Start guessing game
  computer_guess(highest_number)