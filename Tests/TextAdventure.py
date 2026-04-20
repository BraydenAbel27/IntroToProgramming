trophies = 700
pixels = 19800
quad_kills = 499
def rocket_bot_royale():
    print("You are sitting in the back of Mrs. Schulzetenberg's 4th hour government class super bored so you open up your chromebook and go onto the game Rocket Bot Royale. What do you do?")
    print("1. Hop in a ranked match")
    print("2. Hop in a battle royale")
    print("3. Change your mind and go back to doing your work")
    choice1= input("-> ")
    if choice1== "1":
        ranked_match()
    elif choice1 == "2":
        battle_royale()
    elif choice1== "3":
        school_work()
    else:
        print("Invalid choice, choose a real option.")
        rocket_bot_royale()
    return choice1

def ranked_match():
    print("You hop into a ranked match and get a lobby with some pretty good players so you know you have to lock in.")

def battle_royale():
    print("You hop into a battle royale and get a lobby with some bad players so you know this'll be easy if you lock in.")

def school_work():
    print("You try to do your school work but end up falling asleep. When you awake you see the teacher yelling at you for sleeping and she sends you to the office.")
    print("After a quick chat with Mr. Reeves you get sent back to class and you decide that you should just play some Rocket Bot Royale.")
    rocket_bot_royale()


def ranked_drop():
    print("You get the music map and you need to drop somewhere on there. Where do you drop?")
    print("1. Drop early")
    print("2. Drop center")
    print("3. Drop late")
    print("4. Don't drop")
    choice2= input("-> ")
    if choice2== "1":
        
    elif choice2 == "2":
        
    elif choice2== "3":

    elif choice2== "4":

    else:
        print("Invalid choice, choose a real option.")
        ranked_drop()