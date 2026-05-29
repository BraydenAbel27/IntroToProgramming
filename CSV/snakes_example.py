import csv

with open("C:\\Users\\820952\\Documents\\Intro To Programming\\IntroToProgramming\\CSV\\snakes_count_10000.csv", "r") as csv_file:
    file = csv.reader(csv_file)

    average_game = 0
    longest_game = 0
    shortest_game = 0
    num_games = 0
    total_game_time = 0

    next(file)

    for row in file:

        num_games = num_games + 1

        total_game_time = total_game_time + int(row[1])

        if int(row[1]) > longest_game:
            longest_game = int(row[1])

        if int(row[1]) < shortest_game:
            shortest_game = int(row[1])

    average_game = total_game_time / num_games

    print("The average game was " + str(average_game) + " minutes.")
    print("The longest game was " + str(longest_game) + " minutes.")
    print("The shortest game was " + str(shortest_game) + " minutes.")