def hello(): #def defines a function    
    print("This is inside the function")
    print("Still inside the function")
print("This is outside the function")
hello()

def add(x = 0, y = 0):
    return x + y
print(add(67, 2))
my_number = add(5, 6)
print(my_number)
