# Hands-on exercise on List and its built-in methods (append, index, remove, sort)

# Task: Write a menu-driven program to create a Student Records Management System using
#               List and List methods
#  1. Add Student - Take name, roll number, subject and marks as input and store them in a list
#  2. Display students - show all stored students in a readable format
#  3. Search Student - Search for a student by roll number and display if found
#  4. update recored - Update the marks of student using roll number
#  5. Delete Record - Delete a student record using roll number
#  6. Sort Record - Sorting students records by marks or name
#  7. Exit

# for storing students records
# Each student should have [name, roll_no, course, marks]
students_records = []

# 1. Add student
def add_student():
    name = input("Enter student name:")
    roll_no = input("Enter student roll no:")
    course = input("Enter student course: ")
    marks = int(input("Enter student marks:"))
    students_records.append([name, roll_no, course, marks])
    print("Student added successfully...")

# 2. display students
def display_records():
    if students_records:
        print("------------------")
        print("Students records")
        print("------------------")
        for student in students_records:
            print(f"Name: {student[0]}")
            print(f"Roll no: {student[1]}")
            print(f"Course: {student[2]}")
            print(f"Marks: {student[3]}")
            print("-----------------------")
    else:
        print("No record found. Enter records first")

# 3. Search student from record
def search_student():
    # check if student record is not empty
    if students_records:
        roll_no = input("Enter roll no of student:")
        
        for index, student in enumerate(students_records):
            if roll_no == student[1]:  # roll no is at index 1
                return student, index  # students_records.index(student)
        # If no records roll_no matches the input roll_no then return None
        return None, None
    else:
        print("Unable to search. Please enter records first....")
        return None, None  

    
while True:
    print("-----------------------------")
    print("1. Add Student Record.")
    print("2. Display Student Records.")
    print("3. Search Student Record.")
    print("4. Update Student Record.")
    print("5. Delete Student Record.")
    print("6. Sort Records")
    print("7. Exit")
    print("-----------------------------")

    choice = input("Enter your option:")

    if choice == '1':
        # Add Student
        add_student()
    elif choice == '2':
        # Display Students Records
        display_records()
    elif choice == '3':
        # Search student record
        student, _ = search_student()
        if student is not None:
            print("---Student found---")
            print(f"Name: {student[0]}")
            print(f"Roll no: {student[1]}")
            print(f"Course: {student[2]}")
            print(f"Marks: {student[3]}")
        else:
            print("Record not found !!!")
    elif choice == '4':
        # Update student record
        pass
    elif choice == '5':
        # Delete student record
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        # Exit
        break
    else:
        print("Invalid Choice!!!")
