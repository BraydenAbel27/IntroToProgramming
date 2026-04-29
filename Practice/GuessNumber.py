import random

target_number = random.randint(1, 100)
guess = None

print("Guess a random number between 1 and 100")

while guess != target_number:
    try:
        guess = int(input("Enter guess: "))
        if guess < target_number:
            print("Too low.")
        elif guess > target_number:
            print("Too high.")
        else:
            print(f"{target_number} is correct.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
