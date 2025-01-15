
# diary got deletedddddd will try to get it back later!!

# ChatGPT Coding Diary

## Name: Shirley Jiang

### Date: 01/14/25

---

## 1. **Task/Problem Description**

> I want to make a function where the player gets an small chance to get a power up to deal double damage. How can I develop my classes further.

---

## 2. **Initial Approach/Code**

Describe the initial approach you took to solving the problem. If you started writing code, include it here.

```python
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.health = health

class PowerUp:
    def __init__(self, chance=0.2): 
        self.chance = chance

    def activate:

```

> My original plan was to create a class for the player and another class for the power-up. Then I can create a function where it activates. 

> Before using ChatGPT, I created a class for the player and powerup, however I don't know how to apply the powerup.

---

## 3. **Interaction with ChatGPT**

### Questions/Requests to ChatGPT
> How do make an function for the powerup to activate?

> What does random.random() do?

> How can I create art in terminal?

---

## 4. **ChatGPT's Suggestions/Code Changes**

Record the code or suggestions ChatGPT provided. Include any changes or improvements ChatGPT suggested and how it influenced your approach.

```python
import random

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health


class PowerUp:
    def __init__(self, chance=0.2):
        self.chance = chance

    def activate(self):
        if random.random() < self.chance:
            return True
        else:
            return False

if power_up.activate():
    print(f"{player.name} activated a power-up!")
else:
    print(f"{player.name} did not activate the power-up.")
```

```python
# One option is to create ASCII art to represent your player. ASCII art uses characters (like letters, numbers, and symbols) to form pictures.

# Here’s an example of simple ASCII art for a player:

player_art = """
  O
 /|\\
 / \\
"""
print(player_art)
```

- ChatGPT suggested to use random.random(), which generates a random float between 0 and 1. If this float is less than the chance (0.2) the powerup is activated.
- It differed from my original code because I did not consider using if and else.

---

## 5. **Reflection on Changes**
> I believe ChatGPT's suggestions are helpful and relevant because it provided an easy solution to my original problem. Yes, the suggestions improved my code because now my player has an 20% to activate a powerup. ChatGPT suggested how I can use randomized floats and if else to apply my powerup on the player. Yes, i understand why the changes were made.

---
