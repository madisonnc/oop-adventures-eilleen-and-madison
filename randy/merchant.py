from item import HealthPotion, StaminaPotion, AttackBoost

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
