class ShoppingCart:
    def __init__(self):
        self.__items = [] 

    def add_item(self, item):
        if item not in self.__items:
            self.__items.append(item)
            print(f"{item} added to cart.")
        else:
            print(f"{item} already in cart!")

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart!")

    def view_cart(self):  
        if not self.__items:
            print("Cart is empty.")
        else:
            print("Current Cart Items:", self.__items)


cart1 = ShoppingCart()

print("\n--- Shopping Cart Menu ---")
while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        cart1.add_item(item)

    elif choice == "2":
        item = input("Enter item to remove: ")
        cart1.remove_item(item)

    elif choice == "3":
        cart1.view_cart()

    elif choice == "4":
        print("Thanks for Shopping......")
        break

    else:
        print("Invalid choice! Please try again.")
