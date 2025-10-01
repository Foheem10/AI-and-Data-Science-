class Password_Manager:
    def __init__(self, username, password):
        self.username = username       # public attribute
        self.__password = password     # private attribute


    def set_password(self, old, new):
        if self.__password == old:
            self.__password = new
            print("Password updated successfully.")
        else:
            print("Old password is incorrect!")

    # check username
    def __check_username(self, name):
        return self.username == name

    # check password
    def __check_password(self, input_pass):
        return self.__password == input_pass

    
    def login(self, name, password):
        if self.__check_username(name) and self.__check_password(password):
            print("Login successful!")
        else:
            print("Login failed!")


uname = input("Enter username: ")
pwd = input("Enter password: ")
acc1 = Password_Manager(uname, pwd)


print("\n--- Login ---")
name_logn = input("Enter username to login: ")
pass_logn = input("Enter password to login: ")
acc1.login(name_logn, pass_logn)


print("\n--- Change Password ---")
old_pass = input("Enter old password: ")
new_pass = input("Enter new password: ")
acc1.set_password(old_pass, new_pass)

print("\n--- Login After Password Change ---")
name_logn = input("Enter username: ")
pass_logn = input("Enter password: ")
acc1.login(name_logn, pass_logn)
