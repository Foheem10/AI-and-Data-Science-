# Q10: Check if a number is prime

def prime_num(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True 

n = int(input("Enter a number: "))
if prime_num(n):
    print(n, "is Prime")
else:
    print(n, "is Not Prime")
