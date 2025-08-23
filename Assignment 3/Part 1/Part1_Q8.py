# Q8: Area and Circumference of Circle

def circle(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    print("Area of circle:", area)
    print("Circumference of circle:", circumference)

r = float(input("Enter radius: "))
circle(r)
