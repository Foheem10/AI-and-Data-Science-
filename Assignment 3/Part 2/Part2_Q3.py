# Q3: List operations

fruits = ["apple", "raspberry", "pineapple", "cherry"]

# a)
if "apple" in fruits:
    print("'apple' is present at index:", fruits.index("apple"))
else:
    print("'apple' not found")

# b)
fruits[1:3] = ["orange"]
print("After replacing:", fruits)

# c)
fruits.insert(2, "apricot")
print("After inserting apricot:", fruits)

# d)
fruits.extend(["car", "bike", "aeroplane"])
print("Final list:", fruits)
