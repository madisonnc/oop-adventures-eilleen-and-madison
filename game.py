import random
from entities import Player, Slime, BigSlime, HealthPotion, Merchant

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

        while player.health > 0 and enemy.health > 0:
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
            elif action == "7":
                player.use_inventory_item()
            else:
                print("Invalid option. Please choose again.")

            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! You win!")
                player.currency += enemy.currency_reward  
                print(f"{player.name} gains {enemy.currency_reward} gold!")
                drop_item(player)
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
