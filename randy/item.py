class Item:
    def __init__(self, name, effect, price):
        self.name = name
        self.effect = effect
        self.price = price

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion", self.use, price=10)

    def use(self, player):
        heal_amount = 20
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
