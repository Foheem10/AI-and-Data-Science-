# Q6: Check if a number is even or odd

def check_num(num):
    
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

n = int(input("Enter a number: "))
check_num(n)
