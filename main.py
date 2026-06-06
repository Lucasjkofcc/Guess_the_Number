import random
number = random.randint(1, 100)
print("Digit any letter to exit!")
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            print("Restarting the game...")
            number = random.randint(1, 100)
    except ValueError:
        print("Exited Successfully!")
        break