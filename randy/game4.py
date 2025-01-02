# Rock Paper Scissors

import random

class RockPaperScissors:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
    
    def play(self, user_choice):
        computer_choice = random.choice(self.options)
        
        if user_choice == computer_choice:
            return f"tie!"
        
        if (user_choice == 'rock' and computer_choice == 'scissors') or \
           (user_choice == 'paper' and computer_choice == 'rock') or \
           (user_choice == 'scissors' and computer_choice == 'paper'):
            return f"{user_choice} won against {computer_choice}!"
        
        return f"{user_choice} lost against {computer_choice}"

game = RockPaperScissors()

user_choice = input("Enter rock, paper, or scissors: ").lower()

if user_choice not in game.options:
    print("invalid")
else:
    print(game.play(user_choice))