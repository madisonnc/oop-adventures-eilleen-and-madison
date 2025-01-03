from game_classes import Player, Enemies, Slime, BigSlime

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
        print("5. View Money")

        action = input("Enter the number of your choice: ")

        if action == "1":
            player.attack_enemy(slime, attack_type=1)
        elif action == "2":
            player.attack_enemy(slime, attack_type=2)
        elif action == "3":
            player.heal()
        elif action == "4":
            print(f"{player.name} does nothing this turn.")
        elif action == "5":
            player.display_money()
        else:
            print("Invalid option. Please choose again.")

        if slime.health > 0:
            slime.take_turn(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated! Game over.")
            break
        elif slime.health <= 0:
            print(f"{slime.name} has been defeated! You win!")
            player.money += slime.drop_money()  # Add money dropped by slime
            print(f"Total money: {player.money} gold.")
            print(f"Next enemy: {big_slime.name}")
            slime = big_slime  # Switch to Big Slime
            big_slime = None  # No longer use BigSlime class after it appears

start_game()
