def rocket_bot_royale():
    print("You are sitting in the back of Mrs. Schulzetenberg's 4th hour government class super bored so you open up your chromebook and go onto the game Rocket Bot Royale. What do you do?")
    print("1. Hop in a ranked match")
    print("2. Hop in a battle royale")
    print("3. Change your mind and go back to doing your work")
    global choice1
    choice1 = input("-> ")
    if choice1 == "1":
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
    print("You hop into a ranked match with a loadout of 2 flaks, 2 mines, and 1 jetpack and get a lobby with some pretty good players so you know you have to lock in.")
def battle_royale():
    print("You hop into a battle royale with a loadout of 2 flaks, 2 mines, and 1 jetpack and get a lobby with some bad players so you know this'll be easy if you lock in.")
def school_work():
    print("You decide that you gotta lock in for that test tommorrow and do your work")


def ranked_drop():
    print("You get the music map and you need to drop somewhere on there. Where do you drop?")
    print("1. Drop early")
    print("2. Drop center")
    print("3. Drop late")
    print("4. Don't drop")
    global choice2
    choice2 = input("-> ")
    if choice2 == "1":
        ranked_drop_early()
    elif choice2 == "2":
        ranked_drop_center()
    elif choice2== "3":
        ranked_drop_late()
    elif choice2== "4":
        drop_dont()
    else:
        print("Invalid choice, choose a real option.")
        ranked_drop()
    return choice2

def ranked_drop_early():
    print("You drop early and land with 7 other players and get insta killed by all the spamming so you ragequit the game and just do your schoolwork.")
def ranked_drop_center():
    print("You drop center and land with 4 other players and all of you start heading up towards the high ground.")
def ranked_drop_late():
    print("You drop late and land with no one else so you are safe for now and start heading up towards high ground.")
def drop_dont():
    print("You don't drop and die to the water so you decide to just lock in on your schoolwork.")


def br_drop():
    print("You get the map beach 1 and you need to drop somewhere. Where do you drop?")
    print("1. Drop early")
    print("2. Drop center")
    print("3. Drop late")
    print("4. Don't drop")
    global choice3
    choice3 = input("-> ")
    if choice3 == "1":
        br_drop_early()
    elif choice3 == "2":
        br_drop_center()
    elif choice3== "3":
        br_drop_late()
    elif choice3== "4":
        drop_dont()
    else:
        print("Invalid choice, choose a real option.")
        br_drop()
    return choice3

def br_drop_early():
    print("You drop early and land with 10 other players so you use your 2 flaks and get 3 kills and manage to escape.")
def br_drop_center():
    print("You drop center with 1 other players and instantly mine tap him getting a kill and take zero damage")
def br_drop_late():
    print("You drop late with 2 other players who team on you and end up whirlwinding you down into the water. You just close your chromebook and get back to work.")


def ranked_center():
    print("3 players are fighting going up to high ground and 1 is retreating down. What do you do?")
    print("1. Go after the player going down")
    print("2. Go up and fight your way through the 3 players")
    print("3. Sit in the middle and don't move")
    global choice4
    choice4 = input("-> ")
    if choice4 == "1":
        ranked_center_retreat()
    elif choice4 == "2":
        ranked_center_fight()
    elif choice4== "3":
        ranked_center_sit()
    else:
        print("Invalid choice, choose a real option.")
        ranked_center()
    return choice4

def ranked_center_retreat():
    print("You go after the player going down and he sees you and keeps running away getting close to the water.")
def ranked_center_fight():
    print("You go up to fight them and try to get some kills but using their height advantage they take you out. You close your chromebook abd get back to doing your work.")
def ranked_center_sit():
    print("You sit in the middle and 1 of the tanks from above starts shooting at you hitting you once so now you have to fight him")


def ranked_center_low():
    print("The tank keeps running away close to the water and he is escaping. What do you do?")
    print("1. Jetpack into him and hit him with a flak to try kill him")
    print("2. Let him escape")
    global choice5
    choice5 = input("-> ")
    if choice5 == "1":
        ranked_center_low_attack()
    elif choice5 == "2":
        ranked_center_low_escape()
    else:
        print("Invalid choice, choose a real option.")
        ranked_center_low()
    return choice5

def ranked_center_low_attack():
    print("You jetpack towards him but he hits you with a whirlwind and you end up getting killed by the water. You close the game and get back to your work.")
def ranked_center_low_escape():
    print("You let him escape and you go back up towards the middle and see one player coming down to attack you.")


def ranked_center_mid():
    print("You are in the middle of the map fighting one other player and he has the height advantage. What do you do?")
    print("1. Spam all of your weapons at him hoping for the kill")
    print("2. Full send past him to get above him")
    print("3. Go into him with a flak and try to get a kill")
    global choice6
    choice6 = input("-> ")
    if choice6 == "1":
        ranked_center_spam()
    elif choice6 == "2":
        ranked_center_fullsend()
    elif choice6== "3":
        ranked_center_flak()
    else:
        print("Invalid choice, choose a real option.")
        ranked_center_mid()
    return choice6

def ranked_center_spam():
    print("You spam all of your weapons getting the kill but now you have nothing left. On your way up to high ground you get a mine from a crate.")
def ranked_center_fullsend():
    print("You use your jetpack to make it above him but are left at 1 hp with him still attacking from bellow.")
def ranked_center_flak():
    print("You go into him with a flak and he shoots on at the same time so you end up trading kills and both dying. You go back to doing your work.")


def ranked_center_top():
    print("You are at the high ground and there is only 1 other player left. What do you do?")
    print("1. Camp the high ground and wait for the water to rise.")
    print("2. Go down towards him and try to mine tap predict.")
    print("3. Destroy all the high ground so no one can use it.")
    global choice7
    choice7 = input("-> ")
    if choice7 == "1":
        ranked_top_camp()
    elif choice7 == "2":
        ranked_top_mine()
    elif choice7== "3":
        ranked_top_destroy()
    else:
        print("Invalid choice, choose a real option.")
        ranked_center_top()
    return choice7

def ranked_top_camp():
    print("You sit on the high ground shooting shots bellow at him and he can't get up to you so he dunks into the water and you win the game.")
def ranked_top_mine():
    print("You go down to mine tap predict but miss completely and then he kills you.")
def ranked_top_destroy():
    print("You destory all the high ground but he just spams you with whirls and knocks you into the water, killing you.")


def ranked_center_1hp():
    print("You have 1 hp left and the player is attacking you from bellow. What do you do?")
    print("1. Shoot down at him while slowly going up to high ground")
    print("2. Run away and get to high ground")
    print("3. Go into him with no weapons and try to get a kill")
    global choice8
    choice8 = input("-> ")
    if choice8 == "1":
        ranked_1hp_shoot()
    elif choice8 == "2":
        ranked_1hp_run()
    elif choice8 == "3":
        ranked_1hp_charge()
    else:
        print("Invalid choice, choose a real option.")
        ranked_center_1hp()
    return choice8

def ranked_1hp_shoot():
    print("You shoot down getting enough hits to heal up to 2 hp. He shoots a laser hitting you but you survive since you healed. You keep shooting and kill him then head up towards high ground.")
def ranked_1hp_run():
    print("You run up to high ground but he shoots you with a laser killing you.")
def ranked_1hp_charge():
    print("You go into him with no weapons and he easily takes you out.")


def ranked_late():
    print("As you are going toward the middle you see 2 crates falling from the sky and 1 player camping near the water. What do you do?")
    print("1. Get the crates")
    print("2. Go after the player near the water")
    global choice9
    choice9 = input("-> ")
    if choice9 == "1":
        ranked_late_crates()
    elif choice9 == "2":
        ranked_late_chase()
    else:
        print("Invalid choice, choose a real option.")
        ranked_late()
    return choice9

def ranked_late_crates():
    print("You get a flak and a mine from the crates and the tank escapes you so you head up toward the high ground.")
def ranked_late_chase():
    print("You head toward the player to attack him but he starts to run away getting very close to the water.")


def ranked_high_ground():
    print("You make it to the high ground and see 2 teamers camping on top with shields. What do you do?")
    print("1. Shoot up to them and then jetpack into the shield with a flak")
    print("2. Use your mines to destroy their high ground")
    print("3. Just give up and dunk in the water")
    global choice10
    choice10 = input("-> ")
    if choice10 == "1":
        jetpack_flak()
    elif choice10 == "2":
        mine_destory()
    elif choice10 == "3":
        dunk()
    else:
        print("Invalid choice, choose a real option.")
        ranked_high_ground()
    return choice10

def jetpack_flak():
    print("They use a shield but it doesn't matter cause you jetpack into them and kill them with your flak and get the win.")
def mine_destory():
    print("You try to destroy th land with your mines but they use shields and block all of them making you die to the water.")
def dunk():
    print("You think that you have no chance at winning so you just go into the water and lose the game.")


def br_strat():
    print("You need to figure out a game plan. What do you do?")
    print("1. You go up to high ground and camp the whole game")
    print("2. You go hunt for some kills")
    global choice11
    choice11 = input("-> ")
    if choice11 == "1":
        high_ground_strat()
    elif choice11 == "2":
        hunt_strat()
    else:
        print("Invalid choice, choose a real option.")
        br_strat()
    return choice11

def high_ground_strat():
    print("You decide to go up to the high ground and camp to try to win the game.")
def hunt_strat():
    print("You decide that you want some kills so you go looking for some players.")


def hunt_kills():
    print("You drive around the map searching for players and see 2 fighting each other. What do you do?")
    print("1. Let them fight it out")
    print("2. Go try to get the kills")
    global choice12
    choice12 = input("-> ")
    if choice12 == "1":
        hunt_kill_wait()
    elif choice12 == "2":
        hunt_kill_fight()
    else:
        print("Invalid choice, choose a real option.")
        hunt_kills()
    return choice12

def hunt_kill_wait():
    print("You wait for them to finish fighting and 1 player kills the other so now you go to attack him.")
def hunt_kill_fight():
    print("You decide to go in and attack them and since they are such noobs you easily take them both out taking but you get hit to 1hp.")


def br_kill_wait():
    print("There is 1 player below you. How do you attack him? ")
    print("1. You just leave and go up to camp high ground.")
    print("2. You try to clip farm on him with your mines.")
    print("3. You go into him with a flak.")
    global choice13
    choice13 = input("-> ")
    if choice13 == "1":
        leave_kill_camp()
    elif choice13 == "2":
        clip_farm()
    elif choice13 == "3":
        flak_kill()
    else:
        print("Invalid choice, choose a real option.")
        br_kill_wait()
    return choice13

def leave_kill_camp():
    print("You go up to high ground so you can try to camp to win the game.")
def clip_farm():
    print("You go down and try to predict mine tap him but you are not that good at the game so you completely airball and die to the water.")
def flak_kill():
    print("You kill him and then head up to high ground to try to win the game.")


def br_camp():
    print("You make it up to the top of high ground and see 2 crates falling from the sky and a player bellow you. What do you do?")
    print("1. Go get the crates.")
    print("2. Stay on high ground and keep camping.")
    global choice14
    choice14 = input("-> ")
    if choice14 == "1":
        br_crates()
    elif choice14 == "2":
        keep_camping()
    else:
        print("Invalid choice, choose a real option.")
        br_camp()
    return choice14

def br_crates():
    print("You leave high ground to get the crates and the other player takes it with the water rising close bellow you.")
def keep_camping():
    print("Using the high ground you easily camp out the water and get the win.")
          

def player_camping():
    print("There is 1 player left camping high ground with shields and you are bellow him with the water rising. What do you do?")
    print("1. Dunk in the water.")
    print("2. Jetpack flak him.")
    print("3. Use your mines to destroy his high ground.")
    global choice15
    choice15 = input("-> ")
    if choice15 == "1":
        dunk()
    elif choice15 == "2":
        jetpack_flak()
    elif choice15 == "3":
        mine_destory()
    else:
        print("Invalid choice, choose a real option.")
        player_camping()
    return choice15


def br_1hp():
    print("Another player shows up from above and is holding you down to the water while you are 1hp. What do you do?")
    print("1. Dunk in the water.")
    print("2. Go into him with a flak.")
    print("3. Run away.")
    global choice16
    choice16 = input("-> ")
    if choice16 == "1":
        dunk()
    elif choice16 == "2":
        flak_1hp()
    elif choice16 == "3":
        run_away()
    else:
        print("Invalid choice, choose a real option.")
        br_1hp()
    return choice16

def flak_1hp():
    print("You go into him to flak him but since you are 1hp he kills you before you get to him.")
def run_away():
    print("You run away from him but he takes out a laser and since you are 1hp he kills you.")


def br_high_ground():
    print("You head up to high ground and see a player on high ground and 1 right below you. what do you do?")
    print("1. Attack the player below you.")
    print("2. Attack the player on high ground.")
    print("3. Dunk in the water.")
    global choice17
    choice17 = input("-> ")
    if choice17 == "1":
        attack_below()
    elif choice17 == "2":
        attack_above()
    elif choice17 == "3":
        dunk()
    else:
        print("Invalid choice, choose a real option.")
        br_high_ground()
    return choice17

def attack_below():
    print("You go down to attack the player below you letting the other one keep high ground.")
def attack_above():
    print("You go up to high ground to attack the player up there leaving the other one below you.")


def attack_down():
    print("The player below you has nukes and mines. How do you attack?")
    print("1. Spam all of your weapons.")
    print("2. Change your mind and attack the player above.")
    print("3. Mine tap.")
    print("4. Close range flak.")
    global choice18
    choice18 = input("-> ")
    if choice18 == "1":
        br_spam()
    elif choice18 == "2":
        attack_above()
    elif choice18 == "3":
        mine_tap()
    elif choice18 == "4":
        close_range_flak()
    else:
        print("Invalid choice, choose a real option.")
        attack_down()
    return choice18

def br_spam():
    print("As you are spamming all of your weapons he hits you with a mine nuke, killing you.")
def mine_tap():
    print("You keep your distance and shoot a mine tap which hits him killing him.")
def close_range_flak():
    print("You try to get close to use your flak but he uses a mine nuke which kills you instantly.")


def br_1v1():
    print("There is 1 player left above you with shields. What do you do?")
    print("1. Jetpack into him with a flak")
    print("2. Dunk in the water.")
    print("3. Use your mines to destory high ground.")
    global choice19
    choice19 = input("-> ")
    if choice19 == "1":
        jetpack_flak()
    elif choice19 == "2":
        dunk()
    elif choice19 == "3":
        mine_destory()
    else:
        print("Invalid choice, choose a real option.")
        br_1v1()
    return choice19


def attack_up():
    print("You go up to high ground to attack the player up there. What do you do?")
    print("1. Jetpack to secondary high ground to camp.")
    print("2. Use your mines to destory his land.")
    print("3. Dunk in the water.")
    global choice20
    choice20 = input("-> ")
    if choice20 == "1":
        second_ground()
    elif choice20 == "2":
        mine_land()
    elif choice20 == "3":
        dunk()
    else:
        print("Invalid choice, choose a real option.")
        attack_up()
    return choice20

def second_ground():
    print("You get to the second highest point and camp till the end game where you use mine jumps to win the game.")
def mine_land():
    print("You shoot mines at his land but he uses a shield to block them and then the player from bellow comes up and kills you.")





















rocket_bot_royale()
if choice1 == "1":
    ranked_drop()
if choice1 == "1" and choice2 == "2":
    ranked_center()
if choice1 == "1" and choice2 == "2" and choice4 == "1":
    ranked_center_low()
if choice1 == "1" and choice2 == "2" and choice4 == "3":
    ranked_center_mid()
if choice1 == "1" and choice2 == "2" and choice4 == "1" and choice5 == "2":
    ranked_center_mid()
if choice1 == "1" and choice2 == "2" and choice4 == "3" and choice6 == "1":
    ranked_center_top()
if choice1 == "1" and choice2 == "2" and choice4 == "1" and choice5 == "2" and choice6 == "1":
    ranked_center_top()
if choice1 == "1" and choice2 == "2" and choice4 == "3" and choice6 == "2":
    ranked_center_1hp()
if choice1 == "1" and choice2 == "2" and choice4 == "1" and choice5 == "2" and choice6 == "2":
    ranked_center_1hp()
if choice1 == "1" and choice2 == "2" and choice4 == "3" and choice6 == "2" and choice8 == "1":
    ranked_center_top()
if choice1 == "1" and choice2 == "2" and choice4 == "1" and choice5 == "2" and choice6 == "2" and choice8 == "1":
    ranked_center_top()
if choice1 == "1" and choice2 == "3":
    ranked_late()
if choice1 == "1" and choice2 == "3" and choice9 == "2":
    ranked_center_low()
if choice1 == "1" and choice2 == "3" and choice9 == "2" and choice5 == "2":
    ranked_center_mid()
if choice1 == "1" and choice2 == "3" and choice9 == "2" and choice5 == "2" and choice6 == "1":
    ranked_center_top()
if choice1 == "1" and choice2 == "3" and choice9 == "2" and choice5 == "2" and choice6 == "2":
    ranked_center_1hp()
if choice1 == "1" and choice2 == "3" and choice9 == "2" and choice5 == "2" and choice6 == "2" and choice8 == "1":
    ranked_center_top()
if choice1 == "1" and choice2 == "3" and choice9 == "1":
    ranked_high_ground()
if choice1 == "2":
    br_drop()
if choice1 == "2" and choice3 == "2":
    br_strat()
if choice1 == "2" and choice3 == "2" and choice11 == "2":
    hunt_kills()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "1":
    br_kill_wait()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "1" and choice13 == "1":
    br_camp()
if choice1 == "2" and choice3 == "2" and choice11 == "1":
    br_camp()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "1" and choice13 == "1" and choice14 == "1":
    player_camping()
if choice1 == "2" and choice3 == "2" and choice11 == "1" and choice14 == "1":
    player_camping()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "2":
    br_1hp()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "1" and choice13 == "3":
    br_high_ground()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "1" and choice13 == "3" and choice17 == "1":
    attack_down()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "1" and choice13 == "3" and choice17 == "1" and choice18 == "3":
    br_1v1()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "1" and choice13 == "3" and choice17 == "2":
    attack_up()
if choice1 == "2" and choice3 == "2" and choice11 == "2" and choice12 == "1" and choice13 == "3" and choice17 == "1" and choice18 == "2":
    attack_up()
if choice1 == "2" and choice3 == "1":
    br_strat()
if choice1 == "2" and choice3 == "1" and choice11 == "2":
    hunt_kills()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "1":
    br_kill_wait()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "1" and choice13 == "1":
    br_camp()
if choice1 == "2" and choice3 == "1" and choice11 == "1":
    br_camp()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "1" and choice13 == "1" and choice14 == "1":
    player_camping()
if choice1 == "2" and choice3 == "1" and choice11 == "1" and choice14 == "1":
    player_camping()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "2":
    br_1hp()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "1" and choice13 == "3":
    br_high_ground()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "1" and choice13 == "3" and choice17 == "1":
    attack_down()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "1" and choice13 == "3" and choice17 == "1" and choice18 == "3":
    br_1v1()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "1" and choice13 == "3" and choice17 == "2":
    attack_up()
if choice1 == "2" and choice3 == "1" and choice11 == "2" and choice12 == "1" and choice13 == "3" and choice17 == "1" and choice18 == "2":
    attack_up()
