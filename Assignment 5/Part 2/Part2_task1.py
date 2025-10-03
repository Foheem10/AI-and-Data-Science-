# Parent class
class Animal:
    def make_sound(self):
        print("Animals make different sounds.")

# Child class
class Dog(Animal):
    def make_sound(self):
        print("Dog Make sound Like 'Bark!'")


dog1 = Dog()

print("\n--- Single Level Inheritance Example ---")
print("-------------------------------------------")
dog1.make_sound()
print("-------------------------------------------")
