from test import Player, Slime, BigSlime
import random

def start_game():
    player_name = input("What's your name? ")
    player = Player(name=player_name, health=100, attack=5, inventory=[], stamina=50, money=0)

    slime = Slime()
    big_slime = BigSlime()

    while player.health > 0:
        print("\n------------------")
        print(f"{player.name}'s turn")
        print(f"Health: {player.health}, Stamina: {player.stamina}")
        print(f"Enemy: {slime.name} | Health: {slime.health}")

        print("\nWhat would you like to do?")
        print("1. Attack (Light Attack - 10 Stamina)")
        print("2. Attack (Heavy Attack - 20 Stamina)")
        print("3. Heal (10 Health - 10 Stamina)")
        print("4. Do Nothing")

        action = input("Enter the number of your choice: ")

        if action == "1":
            player.attack_enemy(slime, attack_type=1)
        elif action == "2":
            player.attack_enemy(slime, attack_type=2)
        elif action == "3":
            player.heal()
        elif action == "4":
            print(f"{player.name} does nothing this turn.")
        else:
            print("Invalid option. Please choose again.")

        if slime.health > 0:
            enemy_action = random.choice([1, 2, 3]) 
            if enemy_action == 1:
                damage = random.randint(5, 10)
                print(f"{slime.name} attacks! {player.name} takes {damage} damage.")
                player.take_damage(damage)
            elif enemy_action == 2:
                print(f"{slime.name} is too tired to attack this turn.")
            elif enemy_action == 3:
                heal = random.randint(5, 10)
                slime.health += heal
                print(f"{slime.name} heals for {heal} health.")
            
        if player.health <= 0:
            print(f"{player.name} has been defeated! Game over.")
            break
        elif slime.health <= 0:
            print(f"{slime.name} has been defeated! You win!")
            break

start_game()
