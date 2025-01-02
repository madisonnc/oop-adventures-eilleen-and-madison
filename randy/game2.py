# Number Guesser Game

import random

class NumberGuesser:
    def __init__(self):
        self.num_guess = random.randint(1, 10)
    
    def guess(self, user_guess):
        if user_guess == self.num_guess:
            return "correct"
        else:
            return f"incorrect"

game = NumberGuesser()
user_guess = int(input("Guess the number between 1 and 10: "))
print(game.guess(user_guess))