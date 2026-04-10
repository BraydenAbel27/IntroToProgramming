answer1 = int(input("What is 9*7? "))
answer2 = int(input("What is 121/11? "))
answer3 = int(input("What is 5**3? "))
answer4 = input("What is the largest city in Minnesota? ")
answer5 = input("What is the capital of Minnesota? ")
answer6 = input("What is the best fast food restaurant? ")
answer7 = int(input("What is 6*7? "))
answer8 = input("Who is the president of the US? ")
answer9 = input("What is the most entertaining sport to watch? ")
answer10 = input("What is the best video game? ")

def tally_score():
    score = 0
    if answer1 == 63:
        score += 1
    if answer2 == 11:
        score += 1
    if answer3 == 125:
        score += 1
    if answer4 == "Minneapolis":
        score += 1
    if answer5 == "St. Paul":
        score += 1
    if answer6 == "Culver's":
        score += 1
    if answer7 == 42:
        score += 1
    if answer8 == "Trump" or answer8 == "Donald Trump":
        score += 1
    if answer9 == "Hockey":
        score += 1
    if answer10 == "Minecraft" or answer10 == "Rocket Bot Royale":
        score += 1
    return score

print("Your score is", tally_score(), "out of 10")