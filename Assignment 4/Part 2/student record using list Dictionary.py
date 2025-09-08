# Part 2
# Student Records Management System (SRMS) using List of Dictionaries

records = []   # list of dictionaries

# 1. Add Student
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter student roll no: ")
    course = input("Enter student course: ")
    marks = int(input("Enter student marks: "))
    
    student = {
        "Name": name,
        "Roll no": roll_no,
        "Course": course,
        "Marks": marks
    }
    records.append(student)
    print("Student added successfully....")

# 2. Display Students
def display_records():
    if records:
        print("-----------------------")
        print("Student Records")
        print("-----------------------")
        for student in records:
            print(student)  
        print("-----------------------")
    else:
        print("No record found, Enter records first")

# 3. Search Student
def search_student():
    if records:
        roll_no = input("Enter roll no of student: ")
        for index, student in enumerate(records):
            if roll_no == student["Roll no"]:
                return student, index
        return None, None
    else:
        print("Empty Record")

# 4. Update Record
def update_marks():
    student_found, index = search_student()
    if student_found is not None:
        print("---------------")
        print("Record Found")
        print("---------------")
        print(f"Name: {student_found['Name']}")
        print(f"Roll No: {student_found['Roll no']}")
        print(f"Course: {student_found['Course']}")
        print(f"Marks: {student_found['Marks']}")
        print("---------------")

        new_marks = int(input("Enter marks to update: "))
        records[index]["Marks"] = new_marks
        print("Record Successfully updated...")
    else:
        print("Record not Found! \nUnable to update")

# 5. Delete Record
def delete_record():
    student_found, _ = search_student()
    if student_found is not None:
        records.remove(student_found)
        print("Deleted Record successfully")
    else:
        print("Record not found! \nUnable to delete")

# 6. Sort Records
def sort_records():
    if records:
        records.sort(key=lambda x: x["Marks"], reverse=True)
        print("Records sorted by Marks successfully....")
    else:
        print("Empty Records!!! \nUnable to Sort")

# Menu
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

    option = input("Enter your option: ")

    if option == '1':
        add_student()

    elif option == '2':
        display_records()

    elif option == '3':
        student_, _ = search_student()
        if student_ is not None:
            print("---Student found---")
            print(f"Name: {student_['Name']}")
            print(f"Roll no: {student_['Roll no']}")
            print(f"Course: {student_['Course']}")
            print(f"Marks: {student_['Marks']}")
        else:
            print("Record not found !!!")

    elif option == '4':
        update_marks()

    elif option == '5':
        delete_record()

    elif option == '6':
        sort_records()

    elif option == '7':
        break

    else:
        print("Invalid Choice!!!")
