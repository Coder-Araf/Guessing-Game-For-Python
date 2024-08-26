import random

diceRoll = True

while diceRoll:
    print(random.randint(1,6))
    playA = input("Are you continue to write [y/n] : ")
    if playA == "y" or playA == "Y":
        continue
    else:
        print("Game Over")
        break