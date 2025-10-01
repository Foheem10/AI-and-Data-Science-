# function Tutorial

# ---------------
# 1
# ---------------
### Function definition withour input data and return
##def my_function():
##    """
##        Function Tutorial
##    """
##    print("I am from Pakistan")
##
##
##my_function()

# ---------------
# 2
# ---------------
### Function definition with input data and no return
##def full_name(fname, lname):
##    """
##        Function with input data (arguments/parameters)
##    """
##    full_name = fname + ' ' + lname
##    print(full_name)
##    
### function calling
##full_name("Raja", "Ahsan")
##
### function calling
##full_name("Shahid", "Afridi")

# ---------------
# 3
# ---------------

### function definition with input data and return
##def full_name(fname, lname):
##    """
##        Function with input data and return statement
##    """
##    full_name = fname + " " + lname
##    return full_name
##
### function call
##name = full_name("Raja", "Ahsan")
##print(name)


# ----------------
# 4
# ----------------
##def Nationality(country = "Pakistan"):
##    print("I am from " + country)
##
##Nationality()
##Nationality("Karachi")


# -------------
# 5. Lab Task
# -------------
# Create seperate functions to compute Area an Circumference of a circle
# area()  -> pi * r^2
# circumference()  -> 2 * pi * r

def area(r):
    """
        Compute the Area of Circle
        Input -> Radius of Circle
        Output -> Area of circle 
    """
    area = 3.14 * r ** 2
    return area

def circumference(r):
    """
        Compute the circumference of Circle
        Input -> Radius of Circle
        Output -> Circumference of circle
    """
    circumference = 2 * 3.24 * r
    return circumference

# function calling
area_of_circle = area(5)
print(f"Area of circle = {area_of_circle:.2f}")
circum_of_circle = circumference(5)
print(f"Circumference of Circle = {circum_of_circle:.2f}")
