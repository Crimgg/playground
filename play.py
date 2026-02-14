import random
value = random.randint(1, 100)
guess = 0 
print("Guess a number between 1-100: ")
while guess != value:
    try:
        guess = int(input(""))
    except:
        print("Type a number")
        continue 
    if guess == value:
        print("correct")
    if guess > value:
        print("Too high")
    if guess < value:
        print("Too low")
    if guess >= 101:
        print("Outside of Boundry")
    if guess <= 0:
        print("Outside of Boundry")
