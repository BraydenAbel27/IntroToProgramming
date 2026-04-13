diameter = float(input("What is the diameter of the coin in mm? "))
if diameter >= 24.26:
    print("Quarter")
elif diameter >= 21.21:
    print("Nickel")
elif diameter >= 19.05:
    print("Penny")
elif diameter >= 17.91:
    print("Dime")
else:
    print("Not a coin")