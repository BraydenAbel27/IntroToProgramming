fruits = ["apple", "banana", "kiwi"] #list

print(fruits[1]) #prints second thing in list
print(fruits[0]) #prints first thing in list
print(fruits[2]) #prints third thing in list
print(fruits[-1]) #prints the last thing in list
print(fruits[-3]) #prints third to last thing in list

fruits.append("strawberry") #adds something to the end of a list
fruits.insert(1, "mango") #adds something to a specific spot in a list
fruits.remove("strawberry") #removes something by name from a list
fruits.pop(3) #removes something by index in a list
fruits.clear() #clears the wholoe list

print(len(fruits)) #tells you how many things in a list