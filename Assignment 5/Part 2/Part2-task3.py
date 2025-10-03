# GrandParent class
class GrandParent:
    def family_name(self):
        print("Family Name: Khawja")

# Parent class
class Parent(GrandParent):
    def occupation(self):
        print("Parent's Occupation: Private Employee")

# Child class 
class Child(Parent):
    def hobby(self):
        print("Child's Hobby: Coding")


c1 = Child()

print("\n-----------------------------")
c1.family_name()
c1.occupation() 
c1.hobby()      
print("-----------------------------")
