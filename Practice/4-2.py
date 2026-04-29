for letter in "hello":
    print(letter)

for i in range(5):
    print(i)

numbers = [2, 4, 6, 8]
total = 0
for num in numbers:
    total += num
print(total)

numbers = [1, 2, 3, 4, 5]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

for i in range(5): #break stops the loop
    if i == 3:
        break
    print(i)

for i in range(5): # continue skips the said iteration then continues
    if i == 3:
        continue
    print(i)