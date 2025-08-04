
print('Q.1: Arithmetic Operators')
a = 15
b = 4
print("Addition: a + b =", a + b)
print("Subtraction: a - b =", a - b)
print("Multiplication: a * b =", a * b)
print("Division: a / b =", a / b)
print("Floor Division: a // b =", a // b)
print("Modulus: a % b =", a % b)
print("Exponentiation: a ** b =", a ** b)


print('Q.2: Arithmetic Assignment Operators')
x = 10
print("Initial value of x:", x)
x += 5
print("After x += 5:", x)
x *= 2
print("After x *= 2:", x)
x -= 4
print("After x -= 4:", x)
x /= 2
print("After x /= 2:", x)


print('Q.3: Comparison Operators')
a = 7
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


print('Q.4: Logical Operators')
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)


print ('Q.5: Membership Operators')
institute = "Saylani Mass IT"

print("’s’ in institute:", "s" in institute)
print("'Saylani' in institute:", "Mass" in institute)
print("'Saylani' not in institute:", "Saylani" not in institute)


print('Q.5: Identity Operators')
a = 25
b = 25
c = 100
print("a is b:", a is b)
print("a is c:", a is c)
print("c is not b:", c is not b)

print("BONUS CHALLENGE")

# Taking username and password as input
username = input("Enter your username: ")
password = input("Enter your password: ")

# comparing username and password
if username == "Talha" and password == "Axiom123":
    print("Login Succesfull")
else:
    print("Invalid username or password.")
