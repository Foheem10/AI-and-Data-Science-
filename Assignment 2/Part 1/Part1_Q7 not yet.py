
num_1 = float(input("\nEnter first number: "))
optr = input("Enter operator (+,-,x,/): ")
num_2 = float(input("Enter second number: "))

if optr == "+":
    print("Result:", num_1 + num_2)

elif optr == "-":
    print("Result:", num_1 - num_2)

elif optr == "x" or "*":
    print("Result:", num_1 * num_2)

elif optr == "/":
    if num_2 != 0:
        print("Result:", num_1 / num_2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
