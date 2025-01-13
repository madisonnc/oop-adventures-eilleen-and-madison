import random
import sys
import os
from randy.player import Player
from randy.enemies import Slime, BigSlime
from randy.merchant import Merchant
from randy.item import HealthPotion

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