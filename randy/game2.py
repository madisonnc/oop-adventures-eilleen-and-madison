import random

class Player:
    def __init__(self, name, health, attack, inventory, stamina):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = inventory
        self.stamina = stamina
    
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

def choose_enemy():
    print("\nChoose an enemy to fight:")
    print("1. Slime")
    print("2. Big Slime")
    print("3. Exit (quit the game)")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        return Slime()
    elif choice == "2":
        return BigSlime()
    elif choice == "3":
        print("You chose to exit the game.")
        exit() 
    else:
        print("Invalid choice. Please choose again.")
        return choose_enemy()  

def start_game():
    player_name = input("What's your name? ")
    player = Player(name=player_name, health=100, attack=5, inventory=[], stamina=50)

    while player.health > 0:
        enemy = choose_enemy()  

        print(f"\nA wild {enemy.name} appears!\n")

        while player.health > 0 and enemy.health > 0:
            print("\n------------------")
            print(f"{player.name}'s turn")
            print(f"Health: {player.health}, Stamina: {player.stamina}")
            print(f"Enemy: {enemy.name} | Health: {enemy.health}")

            print("1. Attack (Light Attack - 10 Stamina)")
            print("2. Attack (Heavy Attack - 20 Stamina)")
            print("3. Heal (10 Health - 10 Stamina)")
            print("4. Regenerate Stamina (Costs 10 Stamina to regain 20 Stamina)")
            print("5. Escape (Attempt to escape from the battle)")
            print("6. Do Nothing")

            action = input("Enter the number of your choice: ")

            if action == "1":
                player.attack_enemy(enemy, attack_type=1)
            elif action == "2":
                player.attack_enemy(enemy, attack_type=2)
            elif action == "3":
                player.heal()
            elif action == "4":
                player.regenerate_stamina()
            elif action == "5":
                if player.attempt_escape(enemy):
                    break  
            elif action == "6":
                print(f"{player.name} does nothing this turn.")
            else:
                print("Invalid option. Please choose again.")
            
            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! You win!")
                break

            if enemy.health > 0:
                enemy_action = random.choice([1, 2, 3]) 
                if enemy_action == 1:  
                    damage = random.randint(5, 10)
                    print(f"{enemy.name} attacks! {player.name} takes {damage} damage.")
                    player.take_damage(damage)
                elif enemy_action == 2:  
                    print(f"{enemy.name} does nothing this turn.")
                elif enemy_action == 3:  
                    heal = random.randint(5, 10)
                    enemy.health += heal
                    print(f"{enemy.name} heals for {heal} health.")
        
        if player.health <= 0:
            print(f"{player.name} has been defeated! Game over.")
            break

start_game()
