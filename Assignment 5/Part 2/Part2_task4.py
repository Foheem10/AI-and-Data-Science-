# Father class
class Father:
    def skills(self):
        return "Scientist"

# Mother class
class Mother:
    def skills(self):
        return "Freelancer"

# Child class (inherits both)
class Child(Father, Mother):
    def skills(self):
        return "Scientist and Freelancer"


# 🔹 Create objects
f1 = Father()
m1 = Mother()
c1 = Child()

print("\n------------------------------")
print("Father Skills:", f1.skills())
print("Mother Skills:", m1.skills())
print("Child Skills:", c1.skills())
print("------------------------------")
