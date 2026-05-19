with open("C:\\Users\\820952\\Documents\\Intro To Programming\\IntroToProgramming\\Assignments\\names.txt", "r") as file:
    lines = file.readlines()
name_to_search = input("Enter a name to search for: ").lower()
search_lines = []
for index, line in enumerate(lines):
    if name_to_search in line.lower():
        search_lines.append(index + 1)
if search_lines:
    print(f"{name_to_search.capitalize()} found on lines: {', '.join(map(str, search_lines))}")
else:
    print(f"{name_to_search.capitalize()} not found...")