import random
player = input(print("what's your name? "), [])

class player:
    def __init_(self, name, health, attack, inventory, stamina):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = inventory
        self.stamina = stamina
    
    def take_damage(self, damage):
        self.health -= damage
        return damage

    def attack_enemy(self, enemy):
        attack = [{
            def atk1():
                damage = 5
                if self.stamina >= 10:
                    enemy.take_damage(damage)
                    self.stamina -= 10
                else: 
                    print(f"{self.name} is too tired to attack.")
}, {
    def atk2():
        damage = 10
        if self.stamina >= 20:
            enemy.take_damage(damage)
            self.stamina -= 20
        else: 
            print(f"{self.name} is too tired to attack.")
}]

class enemies:
    def __init__(self, name, attack, health, stamina):
        self.name = name
        self.attack = attack
        self.health = health
        self.stamina = stamina

    def take_damage(self, damage):
        self.health -= damage
        return damage

class Slime(Enemy):
    def __init__(self, name="Slime"):
        super().__init__(health=40, stamina=40)
    def take_damage -= damage():
        if self.health == 0:
            player.stamina += 50

class BigSlime(Enemy):
    def __init__(self, name="Big Slime"):
        super().__init__(health=69, stamina=69)