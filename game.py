import random
from entities import Player, Enemies, Slime, BigSlime

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

if __name__ == "__main__":
    start_game()
