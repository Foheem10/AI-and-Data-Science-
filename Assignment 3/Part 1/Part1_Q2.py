# 2. Check Positive, Negative or Zero

def check_number(num):
    if num > 0:
        print(num, "is Positive")    
    elif num < 0:
        print(num, "is Negative")
    else:
        print(num, "is Zero")

num = int(input("Enter a number: "))
check_number(num)
