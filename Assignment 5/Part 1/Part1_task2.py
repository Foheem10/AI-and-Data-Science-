class Student:
    def __init__(self, name, roll_no, marks):
        # Private attributes
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    # Getter methods
    def get_name(self):
        return self.__name

    def get_rollno(self):
        return self.__roll_no

    def get_marks(self):
        return self.__marks

    # Setter method for marks
    def set_marks(self, marks):
        if  0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid Marks! Must be between 0 and 100.")


print("\n--- Enter Student Data ---")

name1 = input("Enter name of student 1: ")
roll1 = int(input("Enter roll no of student 1: "))
marks1 = int(input("Enter marks of student 1: "))

s1 = Student(name1, roll1, marks1)

name2 = input("\nEnter name of student 2: ")
roll2 = int(input("Enter roll no of student 2: "))
marks2 = int(input("Enter marks of student 2: "))
s2 = Student(name2, roll2, marks2)


print("\n--- Student Objects ---")
print("Name:", s1.get_name(), "| Roll No:", s1.get_rollno(), "| Marks:", s1.get_marks())
print("Name:", s2.get_name(), "| Roll No:", s2.get_rollno(), "| Marks:", s2.get_marks())


print("\n--- Update Marks ---")
new_marks1 = int(input(f"Enter new marks for {s1.get_name()}: "))
s1.set_marks(new_marks1)

new_marks2 = int(input(f"Enter new marks for {s2.get_name()}: "))
s2.set_marks(new_marks2)


print("\n--- After Updating ---")
print("Name:", s1.get_name(), "| Roll No:", s1.get_rollno(), "| Marks:", s1.get_marks())
print("Name:", s2.get_name(), "| Roll No:", s2.get_rollno(), "| Marks:", s2.get_marks())

