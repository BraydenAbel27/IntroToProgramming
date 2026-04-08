num = 4 #global scope

def my_function():
    global num #uses global variable in local scope
    num += 1 #local scope
    
my_function()
my_function()

print(num)