import random

class Player:
    def __init__(self, name, health, attack, inventory, stamina, currency):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = inventory
        self.stamina = stamina
        self.currency = currency 
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_enemy(self, enemy, attack_type):
        if attack_type == 1:  
            damage = 5
            if self.stamina >= 10:
                enemy.take_damage(damage)
                self.stamina -= 10
                print(f"{self.name} attacks with a light attack! {enemy.name} takes {damage} damage.")
            else:
                print(f"{self.name} doesn't have enough stamina to attack.")
        elif attack_type == 2: 
            damage = 10
            if self.stamina >= 20:
                enemy.take_damage(damage)
                self.stamina -= 20
                print(f"{self.name} attacks with a heavy attack! {enemy.name} takes {damage} damage.")
            else:
                print(f"{self.name} doesn't have enough stamina for a heavy attack.")

    def heal(self):
        heal_amount = 10
        if self.stamina >= 10:
            self.health += heal_amount
            self.stamina -= 10
            print(f"{self.name} heals for {heal_amount}. Health is now {self.health}.")
        else:
            print(f"{self.name} doesn't have enough stamina to heal.")

    def regenerate_stamina(self):
        if self.stamina >= 10:
            regain = 30
            self.stamina += regain
            self.stamina -= 10  
            print(f"{self.name} regenerates stamina. Stamina is now {self.stamina}.")
        else:
            print(f"{self.name} doesn't have enough stamina to regenerate more.")

    def attempt_escape(self, enemy):
        escape_chance = random.randint(1, 100)
        if escape_chance <= self.stamina:
            print(f"{self.name} successfully escapes from {enemy.name}!")
            return True  
        else:
            print(f"{self.name} failed to escape! {enemy.name} attacks!")
            damage = random.randint(5, 10)  
            self.take_damage(damage)
            return False  

    def use_inventory_item(self):
        if not self.inventory:
            print("Your inventory is empty!")
            return
        print("Your inventory contains:")
        for index, item in enumerate(self.inventory, 1):
            print(f"{index}. {item.name}")

        choice = input("Choose an item to use: ")
        try:
            item_choice = int(choice) - 1
            if item_choice >= 0 and item_choice < len(self.inventory):
                item = self.inventory[item_choice]
                item.use(self)
                self.inventory.remove(item) 
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")

    def buy_item(self, item):
        if self.currency >= item.price:
            self.currency -= item.price
            self.inventory.append(item)
            print(f"{self.name} bought a {item.name} for {item.price} gold!")
        else:
            print(f"{self.name} doesn't have enough gold to buy {item.name}.")

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