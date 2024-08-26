import random
random_num = random.randrange(1,20)
user_num = int(input("Enter Your Number: "))

if random_num < user_num:
    print(f"{random_num}, Sorry, Your Number is High")
elif random_num > user_num:
    print(f"{random_num}, Sorry, Your Number is too Low")
else:
    print(f"{random_num}, Congratulations... You Number is correct.")

print("Thanks...")