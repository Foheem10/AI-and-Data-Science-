# while loop tutorial

# Tutorial 1: use while loop to print numbers in descending order (from 10 to 1)

number = 10

while number > 0:
    print(number)
    number -= 1   # same as number = number -1


# Tutorial 2: use while loop to keep asking user to input password until the correct
# password is inserted

while True:
    pswd = input("Enter password: ")

    if pswd == "Axiom09":
        print("Input password is correct")
        break
