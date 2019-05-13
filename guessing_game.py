"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("Welcome Player")
    user_ends = False
    highest = float('inf')
    total_chances = 5
    while(not user_ends):
      answer = random.randint(1,10)
      if highest != float('inf'):
        print("The highest score is ",highest)
      guesses = 0
      game_over = False
      while(True):
        if total_chances - guesses <= 2:
          print("you have only ", total_chances-guesses , " more chance(s)")
        guess = input("Guess a number between 1 and 10 inclusive")
        try:
          guess = int(guess)
          if guess < 1 or guess > 10:
            raise ValueError("Stay within 1 and 10 for now")
          guesses += 1
          if guess > answer:
            print("It's lower")
          elif guess < answer:
            print("It's higher")
          elif guess == answer:
            print("You got it")
            print("You got it in {} guesses".format(guesses))
            if guesses < highest:
              print("You are the highest scorer till now")
              highest = guesses
          if guesses == total_chances or guess == answer:
            if guess != answer:
              print("Sorry you ran out of chances")
              print("The correct answer was ",answer)
            while True:
              play_again = input("Do you want to play again?[y]es or [n]o")
              if play_again.lower() != "y" and play_again.lower() != "n":
                print("Not a valid input")
                continue
              if play_again.lower() == "y":
                user_ends = False
                game_over = True
                break
              elif play_again.lower() == "n":
                user_ends = True
                game_over = True
                break
            if game_over:
              break
        except  ValueError as err:
          print(err)
          print("Invalid Input. Try again")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
