import random

class Player:
    def __init__(self, name, health, attack ):
        self.name = name
        self.health = health
        self.attack = attack
        self.power_up = PowerUp()

class PowerUp:
    def __init__(self, chance=0.2): 
        self.chance = chance

    def activate(self, damage, player):
        if random.random() < self.chance:
            print(f"Powerup activated! {player.name} attacks with double damage!")
            return damage * 2
        else:
            return damage

class Slime(Enemies):
    def __init__(self, name="Slime"):
        slime_art = """
             _______
            /       \\
         ૮ /  ᵔ ᵕ ᵔ  \\ა
          |           |  
          |   \\___/   |
           \\_________/
        """

class BigSlime(Enemies):
    def __init__(self, name="Big Slime"):
        bigslime_art = """
           _________
          /         \\
         /  ᗜ    ᗜ  \\
        |     ---     |  
        |   /     \\   |  
        |   \\_____/   | و
         \\___________/
        """