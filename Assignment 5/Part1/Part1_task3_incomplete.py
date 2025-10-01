class PasswordManager:
    def __init__(self, username, password):
        self.username = username       # public
        self.__password = password     # private


    def set_password(self, old, new):
        if self.__password == old:
            self.__password = new
            print("Password updated successfully!")
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
            return True
        else:
            return False


pm1 = PasswordManager("Ali", "1234")

print("\n--- Login Attempts ---")
print(pm1.login("Ali", "1234"))   # ✅ True
print(pm1.login("Ali", "0000"))   # ❌ False
print(pm1.login("Ahmed", "1234")) # ❌ False

print("\n--- Change Password ---")
pm1.set_password("1234", "abcd")  # ✅ update
print(pm1.login("Ali", "abcd"))   # ✅ True with new password


# INPUT WALA CODE HE YEH 

class PasswordManager:
    def __init__(self, username, password):
        self.username = username       # public attribute
        self.__password = password     # private attribute

    # Method to change password
    def set_password(self, old, new):
        if self.__password == old:
            self.__password = new
            print("Password updated successfully.")
        else:
            print("Old password is incorrect!")

    # Private method: check username
    def __check_username(self, name):
        return self.username == name

    # Private method: check password
    def __check_password(self, input_pass):
        return self.__password == input_pass

    # Public method for login (uses private methods)
    def login(self, name, password):
        if self.__check_username(name) and self.__check_password(password):
            print("Login successful!")
        else:
            print("Login failed!")


# 🔹 Make one object with input
uname = input("Enter username: ")
pwd = input("Enter password: ")
acc1 = PasswordManager(uname, pwd)

# 🔹 Try login
print("\n--- Login ---")
name_try = input("Enter username to login: ")
pass_try = input("Enter password to login: ")
acc1.login(name_try, pass_try)

# 🔹 Try changing password
print("\n--- Change Password ---")
old_pass = input("Enter old password: ")
new_pass = input("Enter new password: ")
acc1.set_password(old_pass, new_pass)

# 🔹 Test login with new password
print("\n--- Login After Password Change ---")
name_try = input("Enter username: ")
pass_try = input("Enter password: ")
acc1.login(name_try, pass_try)

