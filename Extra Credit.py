import random

mario_items = ["star", "mushroom", "skeleton key", "dice"]
computer = random.choice(mario_items)
guessing = True

while guessing:
    user_guess = input("You must match the item randomly generated: star, mushroom, skeleton key, or dice: ")

    if user_guess != computer:
        print("Keep guessing")
    else:
        guessing = False
        print("You win")
        break



