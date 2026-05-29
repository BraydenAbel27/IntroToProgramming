import csv

with open("C:\\Users\\820952\\Documents\\Intro To Programming\\IntroToProgramming\\CSV\\deniro.csv", "r") as file:
    table = csv.DictReader(file)

    score = []
    total_score = 0
    rows = 0
    title = []
    year = []


    for row in table:
        score.append(row["Score"])
        title.append(row["Title"])
        year.append(row["Year"])
        total_score += int(row["Score"])
        rows += 1


    print("The lowest rated movie is " + title[score.index(min(score))] + " with a score of " + min(score) + ".")
    print("The highest rated movie is " + title[score.index(max(score))] + " with a score of " + max(score) + ".")
    print("The average rating of all the movies is " + str(total_score / rows) + ".")
    print("The movie with the longest name is " + title[title.index(max(title, key=len))] + ".")
    print("The longest time between movies is " + str(int(max(year)) - int(min(year))) + " years.")