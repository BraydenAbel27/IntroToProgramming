import csv

#print the number of employees with the grape grower occupation
with open("C:\\Users\\820952\\Documents\\Intro To Programming\\IntroToProgramming\\CSV\\occupation_census.csv", "r", encoding="utf-8") as file:
    table = csv.DictReader(file)

    occupation = []
    employed_census = []
    code = []


    for row in table:
        occupation.append(row["Occupation"])
        employed_census.append(int(row["Employed_census"]))
        code.append(int(row["Code"]))


print("The most common occupation was " + occupation[employed_census.index(max(employed_census))] + " with " + str(max(employed_census)) + " employees.")
print("The least common occupation was " + occupation[employed_census.index(min(employed_census))] + " with " + str(min(employed_census)) + " employees.")
print("The number of grape growers was " + str(employed_census[occupation.index("Grape Grower")]) + ".")
print("The occupation with 14298 employees was " + occupation[employed_census.index(14298)] + ".")
print("The occupation with the code 451311 was " + occupation[code.index(451311)] + ".")
print("The top 5 most common occupations were " + occupation[employed_census.index(max(employed_census))] + ", " + occupation[employed_census.index(sorted(employed_census)[-2])] + ", " + occupation[employed_census.index(sorted(employed_census)[-3])] + ", " + occupation[employed_census.index(sorted(employed_census)[-4])] + ", and " + occupation[employed_census.index(sorted(employed_census)[-5])] + ".")
