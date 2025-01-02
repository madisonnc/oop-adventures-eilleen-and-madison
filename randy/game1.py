# Math Operation Game

import random

class MathGame:
    def __init__(self):
        self.score = 0
        self.rounds = 2
    
    def ask_question(self):
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            correct = x + y
        elif operation == '-':
            correct = x - y
        elif operation == '*':
            correct = x * y
        elif operation == '/':
            while x % y != 0:
                y = random.randint(1, 20)
            correct = x // y  
        
        answer = input(f"{x} {operation} {y}? ")
        try:
            answer = int(answer) 
            if answer == correct:
                print("correct!")
                self.score += 1
            else:
                print(f"incorrect!")
        except ValueError:
            print("invalid interger")
    
    def start_game(self):
        for i in range(self.rounds):
            self.ask_question()
        
        print(f"game over you scored {self.score}/{self.rounds}.")
        
game = MathGame()
game.start_game()