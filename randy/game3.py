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
        if attack_type == 1:  # Light attack
            damage = 10
            if self.stamina >= 10:
                enemy.take_damage(damage)
                self.stamina -= 10
                print(f"{self.name} attacks with a light attack! {enemy.name} takes {damage} damage.")
            else:
                print(f"{self.name} doesn't have enough stamina to attack.")
        elif attack_type == 2:  # Heavy attack
            damage = 15
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
        # Regenerate stamina but cost some health or stamina as a trade-off.
        if self.stamina >= 10:
            regain = 30
            self.stamina += regain
            self.stamina -= 10  # You lose 10 stamina to gain 20
            print(f"{self.name} regenerates stamina. Stamina is now {self.stamina}.")
        else:
            print(f"{self.name} doesn't have enough stamina to regenerate more.")

    def attempt_escape(self, enemy):
        # Chance of escape depends on the player's stamina (or can be fixed chance)
        escape_chance = random.randint(1, 100)
        if escape_chance <= self.stamina:
            print(f"{self.name} successfully escapes from {enemy.name}!")
            return True  # Escape successful
        else:
            print(f"{self.name} failed to escape! {enemy.name} attacks!")
            damage = random.randint(5, 10)  # Enemy counterattack
            self.take_damage(damage)
            return False  # Escape failed

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

def start_game():
    player_name = input("What's your name? ")
    player = Player(name=player_name, health=100, attack=5, inventory=[], stamina=50)

    while player.health > 0:
        # Choose the enemy (could be random or fixed)
        slime = Slime()
        big_slime = BigSlime()
        
        # Randomly choose which enemy to face
        enemy = random.choice([slime, big_slime])

        print("\n------------------")
        print(f"{player.name}'s turn")
        print(f"Health: {player.health}, Stamina: {player.stamina}")
        print(f"Enemy: {enemy.name} | Health: {enemy.health}")

        while enemy.health > 0 and player.health > 0:
            # Ask player for action
            print("\nWhat would you like to do?")
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
                    break  # Escape successful, return to choosing action
            elif action == "6":
                print(f"{player.name} does nothing this turn.")
            else:
                print("Invalid option. Please choose again.")

            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! You win this round.")
                break  # End the current enemy battle

            # Enemy's turn (only if still alive)
            if enemy.health > 0:
                enemy_action = random.choice([1, 2, 3])  # 1: attack, 2: rest, 3: heal
                if enemy_action == 1:  # Enemy attacks
                    damage = random.randint(5, 10)
                    print(f"{enemy.name} attacks! {player.name} takes {damage} damage.")
                    player.take_damage(damage)
                elif enemy_action == 2:  # Enemy does nothing
                    print(f"{enemy.name} does nothing this turn.")
                elif enemy_action == 3:  # Enemy heals
                    heal = random.randint(5, 10)
                    enemy.health += heal
                    print(f"{enemy.name} heals for {heal} health.")
        
        # Check if the game is over
        if player.health <= 0:
            print(f"{player.name} has been defeated! Game over.")
            break

        # Option to continue to the next enemy
        continue_game = input("Do you want to continue fighting? (yes/no): ").strip().lower()
        if continue_game != "yes":
            print(f"Thanks for playing, {player.name}!")
            break  # End the game if the player doesn't want to continue

start_game()

