def get_number():
    n = int(input("Enter a number: "))
    try:
        n = int(n)
    except:
        print("Invalid input. Please enter a valid number.")
        return get_number()
    return n

def divide(x):
    try:
        return 100 / x
    
    except:
        print("Cannot divide by zero. Please enter a non-zero number.")
        get_number()

num = get_number()
print(divide(num))