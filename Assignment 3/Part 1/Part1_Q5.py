# Q5: Function to check age category

def check_age(age):

    if age < 18:
        return "You are Minor"
    elif 18 <= age < 60:
        return "You are Adult"
    else:
        return "You are Senior Citizen"

user_age = int(input("Enter your age: "))
print(check_age(user_age))
