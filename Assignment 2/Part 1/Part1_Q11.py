
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime Number")
