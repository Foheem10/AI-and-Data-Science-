
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("first number is largest")
elif b >= a and b >= c:
    print("second number is largest")
else:
    print("third number is largest")
