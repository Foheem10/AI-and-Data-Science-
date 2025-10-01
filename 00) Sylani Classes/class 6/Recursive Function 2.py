# Recursuve function
# Objective: To compute the factorial of non-negative number using Recursion
# and also check if the number input by user if not < 0 to compute the factorial
# because the factorial of number  < 0 is undefined

num = int(input("Enter a number: "))

def factorial(n):
    if n > 0:  # Base condition
        result = n * factorial(n-1)   # Recursive call [i.e.  factorial(n-1)]
        print(result)
    else:
        result = 1

    return result

# condition to check if user input the number less than 0
# if number < 0, then print Error that factorial of negative number is undefined
# and ask user to input number again
while True:
    if num < 0:
        print("Error! Factorial of negative number is 'undefined'")
        num = int(input("Please Enter number again: "))
    else:
        break

# function call
fact = factorial(num)
print(f"Factorial of {num}! = {fact}")
