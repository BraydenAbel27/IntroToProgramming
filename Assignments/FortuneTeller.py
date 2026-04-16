import random

print("Hello, I am Mysterio the Fortune Teller!")

try:
    lucky_number = int(input("What is your lucky number? "))
    future_years = float(input("How many years into the future do you want to see? "))
    magical_multiplier = float(input("What is your magical multiplier? "))
    age = int(input("How old are you? "))
except ValueError:
    print("Invalid Number. Choose a better one")

random_number = random.randint(1, 100)

fortune = ((lucky_number + future_years) * magical_multiplier - age + random_number)

if fortune < 0:
    print("Your future is not looking very good at all.")
elif fortune < 25:
    print("These next couple years will be rough, but in the future things will go your way.")
elif fortune < 50:
    print("These next couple years will be your best, but things will take a turn for the worst.")
elif fortune < 75:
    print("You do not have very much time left")
elif fortune < 100:
    print("You will live a very long and great life")
elif fortune < 125:
    print("A very life changing event will happen to you in the next couple years")
elif fortune < 150:
    print("You will be sad and lonely forever")
else:
    print("You will be very happy and successful")