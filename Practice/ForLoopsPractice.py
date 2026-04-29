for i in range(10, 0, -1):
    print(i)

numbers = [2, 3, 4, 5, 67, 2, 99, 56, 0, 10]
total = 0
for num in numbers:
    total += num
print(total)

numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)

text = input("Enter a word: ")
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")