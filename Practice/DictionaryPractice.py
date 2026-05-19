student_grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "D",
    "David": "F",
    "Eva": "C"
}
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

student = {"name": "Alice", "age": 16, "grade": "A"}
print(student["name"])
print(student["age"])

student["grade"] = "A+"
print(student["grade"])

movies = {"Whiplash": 2014, "Revenge of the Sith": 2005, "Unstoppable": 2010}
movies["The Empire Strikes Back"] = 1980
print(movies)

fruit_prices = { "apple": 1.00, "banana": 0.75, "cherry": 1.50, "strawberry": 0.30, "blueberry": 0.20}
fruit = input("Enter fruit: ")
if fruit in fruit_prices:
    del fruit_prices[fruit]
print(fruit_prices)

