import random

class MathGame:
    def __init__(self):
        self.score = 0
        self.rounds = 5
    
    def ask_question(self):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            correct = x + y
        elif operation == '-':
            correct = x - y
        elif operation == '*':
            correct = x * y
        elif operation == '/':
            while x % y != 0:
                y = random.randint(1, 100)
            correct = x // y  
        
        answer = input(f"{x} {operation} {y}? ")
        
        try:
            answer = int(answer) 
            if answer == correct:
                print("correct")
                self.score += 1
            else:
                print(f"incorrect")
        except ValueError:
            print("invalid interger")
    
    def start_game(self):
        print("welcome to the math game :)")
        for i in range(self.rounds):
            self.ask_question()
        
        print(f"game over. you scored {self.score}/{self.rounds}.")
        
game = MathGame()
game.start_game()

