import random

class PowerUp:
    def __init__(self, chance=0.2): 
        self.chance = chance

    def activate(self, damage, player):
        if random.random() < self.chance:
            print(f"Powerup activated! {player.name} attacks with double damage!")
            return damage * 2
        else:
            return damage

class Player:
    def __init__(self, name, health, attack, inventory, stamina, currency):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = inventory
        self.stamina = stamina
        self.currency = currency
        self.defeated_enemies = 0 
        self.power_up = PowerUp()

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_enemy(self, enemy, attack_type):
        if attack_type == 1: 
            damage = 5
            if self.stamina >= 10:
                damage = self.power_up.activate(damage, self)
                enemy.take_damage(damage)
                self.stamina -= 10
                print(f"{self.name} attacks with a light attack! {enemy.name} takes {damage} damage.")
            else:
                print(f"{self.name} doesn't have enough stamina to attack.")
        elif attack_type == 2:  
            damage = 10
            if self.stamina >= 20:
                damage = self.power_up.activate(damage, self) 
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
    def __init__(self, name, attack, health, stamina, currency_reward):
        self.name = name
        self.attack = attack
        self.health = health
        self.stamina = stamina
        self.currency_reward = currency_reward

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Health is now {self.health}.")
        return damage

class Slime(Enemies):
    def __init__(self, name="Slime"):
        super().__init__(name, attack=5, health=40, stamina=40, currency_reward=10)

class BigSlime(Enemies):
    def __init__(self, name="Big Slime"):
        super().__init__(name, attack=10, health=69, stamina=69, currency_reward=20)

class Item:
    def __init__(self, name, effect, price):
        self.name = name
        self.effect = effect
        self.price = price

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion", self.use, price=10)

    def use(self, player):
        heal_amount = 30
        player.health += heal_amount
        print(f"{player.name} uses a Health Potion and heals for {heal_amount}!")

class StaminaPotion(Item):
    def __init__(self):
        super().__init__("Stamina Potion", self.use, price=15)

    def use(self, player):
        stamina_restore = 20
        player.stamina += stamina_restore
        print(f"{player.name} uses a Stamina Potion and restores {stamina_restore} stamina!")

class AttackBoost(Item):
    def __init__(self):
        super().__init__("Attack Boost", self.use, price=25)

    def use(self, player):
        attack_increase = 5
        player.attack += attack_increase
        print(f"{player.name} uses an Attack Boost and gains {attack_increase} attack!")

class Merchant:
    def __init__(self):
        self.items_for_sale = [HealthPotion(), StaminaPotion(), AttackBoost()]

    def show_items(self):
        print("Welcome to the merchant!")
        print("Items available for sale:")
        for index, item in enumerate(self.items_for_sale, 1):
            print(f"{index}. {item.name} - {item.price} gold")

    def sell_item(self, player):
        self.show_items()
        choice = input("Enter the number of the item you'd like to buy, or '0' to exit: ")
        if choice == '0':
            print("Leaving the merchant...")
            return
        try:
            item_choice = int(choice) - 1
            if item_choice >= 0 and item_choice < len(self.items_for_sale):
                item = self.items_for_sale[item_choice]
                player.buy_item(item)
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")

def drop_item(player):
    item_drop_chance = random.randint(1, 100)
    if item_drop_chance > 70:  
        item = HealthPotion()
        player.inventory.append(item)
        print(f"{player.name} found a {item.name}!")

def choose_enemy():
    print("\nChoose an enemy to fight:")
    print("1. Slime")
    print("2. Big Slime")
    print("3. Visit Merchant")
    print("4. Exit (quit the game)")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        return Slime()
    elif choice == "2":
        return BigSlime()
    elif choice == "3":
        return "merchant"
    elif choice == "4":
        print("You chose to exit the game.")
        exit()
    else:
        print("Invalid choice. Please choose again.")
        return choose_enemy()

def handle_battle(player, enemy):
    while player.health > 0 and enemy.health > 0:
        display_battle_info(player, enemy)
        handle_player_turn(player, enemy)

        if enemy.health <= 0:
            handle_post_battle(player, enemy)
            break

        if player.health > 0:
            handle_enemy_turn(player, enemy)

def display_battle_info(player, enemy):
    print("\n------------------")
    print(f"{player.name}'s turn")
    print(f"Health: {player.health}, Stamina: {player.stamina}, Gold: {player.currency}")
    print(f"Enemies defeated: {player.defeated_enemies}") 
    print(f"Enemy: {enemy.name} | Health: {enemy.health}")
    print("1. Attack (Light Attack - 10 Stamina)")
    print("2. Attack (Heavy Attack - 20 Stamina)")
    print("3. Heal (10 Health - 10 Stamina)")
    print("4. Regenerate Stamina (Costs 10 Stamina to regain 20 Stamina)")
    print("5. Escape (Attempt to escape from the battle)")
    print("6. Do Nothing")
    print("7. Use Inventory")

def handle_player_turn(player, enemy):
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
            print(f"{player.name} successfully escapes from the battle!")
            return  
    elif action == "6":
        print(f"{player.name} does nothing this turn.")
    elif action == "7":
        player.use_inventory_item()
    else:
        print("Invalid option. Please choose again.")

def handle_enemy_turn(player, enemy):
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

def handle_post_battle(player, enemy):
    print(f"{enemy.name} has been defeated! You win!")
    player.currency += enemy.currency_reward
    print(f"{player.name} gains {enemy.currency_reward} gold!")
    player.defeated_enemies += 1  
    print(f"{player.name} has defeated {player.defeated_enemies} enemies so far.")  
    drop_item(player)

def game_over(player):
    print(f"{player.name} has been defeated! Game over.")

def start_game():
    player_name = input("What's your name? ")
    player = Player(name=player_name, health=100, attack=5, inventory=[], stamina=50, currency=50)

    while player.health > 0:
        choice = choose_enemy()

        if choice == "merchant":
            merchant = Merchant()
            merchant.sell_item(player)
            continue

        enemy = choice
        print(f"\nA wild {enemy.name} appears!\n")
        handle_battle(player, enemy)

        if player.health <= 0:
            game_over(player)
            break

start_game()
