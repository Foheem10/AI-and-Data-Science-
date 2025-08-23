# Q4: Return the largest of three numbers

def largest_number(a, b, c):

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("Largest number is:", largest_number(num1, num2, num3))
