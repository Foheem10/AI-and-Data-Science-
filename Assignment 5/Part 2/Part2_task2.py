# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Child class
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model) 
        self.seats = seats

    # method to display details
    def show_details(self):
        print(f"Car: {self.brand} {self.model}, Seats: {self.seats}")


# 🔹 Create 3 objects of Car
c1 = Car("Toyota", "Corolla", 5)
c2 = Car("Honda", "Civic", 5)
c3 = Car("Suzuki", "Alto", 4)

print("\n-------------------")
c1.show_details()
c2.show_details()
c3.show_details()
print("\n-------------------")