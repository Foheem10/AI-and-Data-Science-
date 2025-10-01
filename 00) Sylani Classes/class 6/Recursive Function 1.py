# Recursive Function
# Objective: To compute the Factorial of non-negative number using Recursion

num = int(input("Enter a number: "))

def factorial(n):
    if n > 0:  # Base condition
        result = n * factorial(n-1)   # Recursive call [i.e.  factorial(n-1)]
        print(result)
    else:
        result = 1

    return result


# function call
fact = factorial(num)
print(f"Factorial of {num}! = {fact}")


