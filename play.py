import random
max = random.randint(10000, 100000)
factorange = max/200

while True:   
    value = random.randint(1, max)
    factors = []
    for i in range(2, value):
        if value%i == 0:
            factors.append(i)
    if len(factors) >= 5:
        break

guess = 0 
print(f"Guess a number between 1-{max}: ")
while guess != value:
    try:
        inp = input("")
        if inp == "I give up":
            print(f"The answer was {value}")
            break
        guess = int(inp)
    except:
        print("Type a number")
        continue 
    if guess == value:
        print("Correct")
        break
    if guess > value:
        print("Too high")
    if guess < value:
        print("Too low")
    if guess > max:
        print("Outside of Boundry")
    if guess <= 0:
        print("Outside of Boundry")
    if abs(guess - value) <= factorange:
        f = factors[random.randint(0, len(factors) - 1)]
        print (f"{f} is a factor")