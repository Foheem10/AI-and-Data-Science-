# exapmle program to check if the number is positive, negative or zero

num = input("Enter a number: ")
num = int(num)

if num > 0:
    # runs if condition1 is True
    print("Number is greater than 0")
elif num < 0:
    # runs if condition1 is False and condition2 is True
    print("Number is less than 0")
else:
    # runs if all of the above conditions are not True
    print("Number is equals to 0")

print("End if code")
