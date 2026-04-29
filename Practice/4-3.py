counter = 1
while counter <= 5:
    print(counter)
    counter += 1

counter = 1
while counter <= 10:
    print(counter)
    if counter == 5:
        break  # Exit the loop when counter reaches 5
    counter += 1

counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue  # Skip the rest of the loop when counter is 3
    print(counter)
