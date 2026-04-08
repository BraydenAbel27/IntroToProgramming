def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_division(x, y):
    return x // y

x = float(input("x: "))
y = float(input("y: "))
operation = input("What operation do you want? ")

if operation == "+":
    print(add(x, y))
if operation == "-":
    print(subtract(x, y))
if operation == "*":
    print(multiply(x, y))
if operation == "/":
    print(divide(x, y))
if operation == "**":
    print(exponent(x, y))
if operation == "%":
    print(modulus(x, y))
if operation == "//":
    print(floor_division(x, y))

