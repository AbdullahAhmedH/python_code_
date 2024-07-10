import random

a = random.randint(1,5)
b = int(input("Enter guess:\n"))

if (a == b):
    print("You win!")
else:
    print("You lose :(\nThe number was:", a)
