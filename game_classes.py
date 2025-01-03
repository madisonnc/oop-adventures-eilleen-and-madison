import random
from randy.game1 import MathGame  # Importing MathGame from game1.py

# Player class
class Player:
    def __init__(self, name, health, attack, inventory, stamina, money):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = inventory
        self.stamina = stamina
        self.money = money  # Currency attribute
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_enemy(self, enemy, attack_type):
        # Ask for math question before attacking
        math_game = MathGame()  # Create an instance of MathGame
        if math_game.ask_question():
            if attack_type == 1:
                damage = 5
                if self.stamina >= 10:
                    enemy.take_damage(damage)
                    self.stamina -= 10
                    print(f"{self.name} attacks with a light attack! {enemy.name} takes {damage} damage.")
                else: 
                    print(f"{self.name} is too tired to attack.")
            elif attack_type == 2:
                damage = 10
                if self.stamina >= 20:
                    enemy.take_damage(damage)
                    self.stamina -= 20
                    print(f"{self.name} attacks with a heavy attack! {enemy.name} takes {damage} damage.")
                else:
                    print(f"{self.name} is too tired to attack.")
        else:
            print(f"{self.name} missed the attack because the math problem was incorrect.")

    def heal(self):
        heal_amount = 10
        if self.stamina >= 10:
            self.health += heal_amount
            self.stamina -= 10
            print(f"{self.name} heals for {heal_amount}. Health is now {self.health}.")
        else:
            print(f"{self.name} is too tired to heal.")

    def display_money(self):
        print(f"{self.name} currently has {self.money} gold.")

# Base class for all enemies
class Enemies:
    def __init__(self, name, attack, health, stamina, drop_rate):
        self.name = name
        self.attack = attack
        self.health = health
        self.stamina = stamina
        self.drop_rate = drop_rate  # Percentage chance to drop money when defeated

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
        return damage

    def drop_money(self):
        # Randomly drops money based on the drop_rate
        if random.randint(1, 100) <= self.drop_rate:
            money_dropped = random.randint(5, 20)  # Enemy drops a random amount of money
            print(f"{self.name} dropped {money_dropped} gold!")
            return money_dropped
        return 0

    def heal(self):
        heal_amount = random.randint(5, 10)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health.")

# Specific enemy classes
class Slime(Enemies):
    def __init__(self, name="Slime"):
        super().__init__(name, attack=5, health=40, stamina=40, drop_rate=50)  # 50% chance to drop money

    def take_turn(self, player):
        # Slime takes a random action (attack, heal, or do nothing)
        action = random.choice([1, 2, 3])
        if action == 1:
            damage = random.randint(5, 10)
            print(f"{self.name} attacks! {player.name} takes {damage} damage.")
            player.take_damage(damage)
        elif action == 2:
            print(f"{self.name} is too tired to attack this turn.")
        elif action == 3:
            self.heal()

class BigSlime(Enemies):
    def __init__(self, name="Big Slime"):
        super().__init__(name, attack=10, health=69, stamina=69, drop_rate=75)  # 75% chance to drop money

    def take_turn(self, player):
        # BigSlime takes a random action (attack, heal, or do nothing)
        action = random.choice([1, 2, 3])
        if action == 1:
            damage = random.randint(10, 15)
            print(f"{self.name} attacks with a heavy strike! {player.name} takes {damage} damage.")
            player.take_damage(damage)
        elif action == 2:
            print(f"{self.name} is too tired to attack this turn.")
        elif action == 3:
            self.heal()
