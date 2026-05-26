import random

def display_leaderboard():
    with open("C:\\Users\\820952\\Documents\\Intro To Programming\\IntroToProgramming\\Assignments\\GuessNumberGame.txt", "r") as file:
        leaderboard = []
        for line in file:
            name, score = line.strip().split(", ")
            leaderboard.append((name, int(score)))
        leaderboard.sort(key=lambda x: x[1])
        print("---Top 5 Players---")
        for name, score in leaderboard[:5]:
            print(f"{name}: {score}")
    play_game()

def play_game():
    input("Press enter to start the game.")
    name = input("What is your name?\n")
    number = random.randint(1, 1001)
    score = 0
    while True:
        guess = int(input("Pick a number from 1 to 1000? "))
        score += 1
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        elif guess == number:
            print(f"You guessed it correctly in {score} tries.")
            break
    with open("C:\\Users\\820952\\Documents\\Intro To Programming\\IntroToProgramming\\Assignments\\GuessNumberGame.txt", "a") as file:
        file.write("\n" + name + ", " + str(score))
        file.close()
    play_again = input("Do you want to play again?\n[y/n]\n")
    if play_again == "y":
        play_game()

display_leaderboard()