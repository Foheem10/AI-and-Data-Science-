# 3. Return Larger of Two Numbers

def larger_number(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

print("Larger is:", larger_number(num1, num2))
