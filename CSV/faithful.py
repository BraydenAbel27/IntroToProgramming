import csv

with open("C:\\Users\\820952\\Documents\\Intro To Programming\\IntroToProgramming\\CSV\\faithful.csv", "r") as file:
    table = csv.DictReader(file)

    wait_time = []
    total_wait = 0
    rows = 0
    eruption_length = []
    total_length = 0


    for row in table:
        wait_time.append(row["Wait"])
        eruption_length.append(row["Length"])
        total_length += float(row["Length"])
        total_wait += int(row["Wait"])
        rows += 1
        

    print("The average eruption time was " + str(total_length / rows) + " minutes.")
    print("The longest eruption time was " + str(max(eruption_length)) + " minutes.")
    print("The shortest eruption time was " + str(min(eruption_length)) + " minutes.")
    print("The average eruption wait was " + str(total_wait / rows) + " minutes.")
    print("The longest eruption wait was " + str(max(wait_time)) + " minutes.")
    print("The shortest eruption wait was " + str(min(wait_time)) + " minutes.")
    print("The eruption time of the longest wait was " + str(eruption_length[wait_time.index(max(wait_time))]) + " minutes with a wait of " + str(max(wait_time)) + " minutes.")