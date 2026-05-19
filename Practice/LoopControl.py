for i in range(1, 21):
    if i == 15:
        break
    print(i)

for num in range(1, 31):
    if num % 2 == 0:
        continue
    print(num)

for i in range(1, 20):
    pass # if statement
    pass # break statement
    print(i)

for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)

numbers = [10, 20, 30, 40, -50, 60]
total = 0
for num in numbers:
    if num < 0:
        break
    total += num
print(total)
