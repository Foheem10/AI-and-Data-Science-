class Employee:
    def __init__(self, name, salary):
        self.__name = name       # private attribute
        self.__salary = 0        # private attribute (default 0)
        self.set_salary(salary)  


    def get_name(self):
        return self.__name


    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            print("Salary updated successfully.")
        else:
            print("Invalid Salary! Must be positive.")


    def show_details(self):
        print(f"Employee Name: {self.__name}, Salary: {self.__salary}")



e1 = Employee("Ali", 50000)
e2 = Employee("Ahmed", 30000)


print("\n--- Employee Details ---")
e1.show_details()
e2.show_details()

print("\n--- Updating Salaries ---")
e1.set_salary(60000)
e2.set_salary(35000)

print("\n--- After Update ---")
e1.show_details()
e2.show_details()
