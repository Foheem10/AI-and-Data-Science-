# Q2: Separate strings, numbers and Boolean data from the list

List = ["Tahir", 44, "AI and Data Science", True]

strings = []
numbers = []
booleans = []

for item in List:

    if type(item) == str:
        strings.append(item)

    elif type(item) == int:
        numbers.append(item)

    elif type(item) == bool:
        booleans.append(item)

print("Strings List:", strings)
print("Numbers List:", numbers)
print("Booleans List:", booleans)
