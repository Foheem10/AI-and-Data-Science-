# Q5: List operations

numbers = [32, 54, 66, 11, 77, 10, 90]

# a)

new_list = []
for num in numbers:
    if num >= 20:
        new_list.append(num)
print("After Removing <20:", new_list)


# b)
new_list.sort()
print("Ascending:", new_list)

new_list.sort(reverse=True)
print("Descending:", new_list)

# c)
total = 0
for num in new_list:
    total = total + num
average = total / len(new_list)
print("Average value:", average)
