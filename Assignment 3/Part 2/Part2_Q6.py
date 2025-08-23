# Q6: List operations

Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

# a)
strings = []
numbers = []

for item in Gadgets:
    if type(item) == str:
        strings.append(item)
    else:
        numbers.append(item)

print("Strings List:", strings)
print("Numbers List:", numbers)

# b)
strings.sort()
print("Ascending order string:", strings)

strings.sort(reverse=True)
print("Descending order string:", strings)

# c) 
strings.sort(key=len)
print("String by Length:", strings)

# d) 
numbers.sort()
print("Ascending Order Numbers:", numbers)

numbers.sort(reverse=True)
print("Descending Order Numbers:", numbers)
