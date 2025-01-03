import random

class Player:
    def __init__(self, name, health, attack, inventory, stamina, money):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = inventory
        self.stamina = stamina
        self.money = money
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
    
    def ask_math_question(self):
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
            while x % y != 0:  # Ensure no fractions
                y = random.randint(1, 100)
            correct = x // y  

        answer = input(f"What is {x} {operation} {y}? ")

        try:
            answer = int(answer)
            if answer == correct:
                print("Correct!")
                return True  # Correct answer, attack proceeds
            else:
                print(f"Incorrect! The correct answer was {correct}.")
                return False  # Incorrect answer, attack fails
        except ValueError:
            print("Invalid input! You must enter an integer.")
            return False  # Invalid input, attack fails

    def attack_enemy(self, enemy, attack_type):
        # Ask math question before allowing attack
        if not self.ask_math_question():
            print(f"{self.name} failed to solve the math question. The attack fails!")
            return  # If the player fails the math question, the attack doesn't proceed
        
        # Proceed with the attack if the math question is correct
        damage = 5 if attack_type == 1 else 10
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    # Additional methods for Player class...
    

class Enemies:
    def __init__(self, name, attack, health, stamina):
        self.name = name
        self.attack = attack
        self.health = health
        self.stamina = stamina

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
        return damage

class Slime(Enemies):
    def __init__(self, name="Slime"):
        super().__init__(name, attack=5, health=40, stamina=40)

class BigSlime(Enemies):
    def __init__(self, name="Big Slime"):
        super().__init__(name, attack=10, health=69, stamina=69)

