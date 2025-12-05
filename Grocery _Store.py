"""Grocery Store Menu:

Create a program where users can:
   1. Add items to their cart.
   2. Remove items.
   3. View the total price.
   4. Exit.

"""

class GroceryStore:
    def __init__(self):
        # available items with prices
        self.items = {
            "apple": 30,
            "banana": 10,
            "milk": 50,
            "bread": 40,
            "rice": 60
        }
        self.cart = {}

    def show_items(self):
        print("\n--- Available Items ---")
        for item, price in self.items.items():
            print(f"{item.capitalize()} - ₹{price}")
        print("-----------------------")

    def add_item(self, item, qty):
        if item not in self.items:
            print("❌ Item not available!")
            return
        
        if item in self.cart:
            self.cart[item] += qty
        else:
            self.cart[item] = qty
        
        print(f"✔ Added {qty} x {item} to cart")

    def remove_item(self, item):
        if item not in self.cart:
            print("❌ Item not in cart!")
            return
        
        del self.cart[item]
        print(f"✔ Removed {item} from cart")

    def view_total(self):
        print("\n--- Cart Summary ---")
        total = 0
        for item, qty in self.cart.items():
            price = self.items[item] * qty
            print(f"{item} x {qty} = ₹{price}")
            total += price
        
        print(f"Total Price: ₹{total}")
        print("----------------------")


def main():
    store = GroceryStore()

    while True:
        print("\n===== Grocery Store Menu =====")
        print("1. View Items")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Total Price")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            store.show_items()
        
        elif choice == "2":
            item = input("Enter item name: ").lower()
            qty = int(input("Enter quantity: "))
            store.add_item(item, qty)
        
        elif choice == "3":
            item = input("Enter item name to remove: ").lower()
            store.remove_item(item)

        elif choice == "4":
            store.view_total()

        elif choice == "5":
            print("Thank you! Visit again 😊")
            break

        else:
            print("❌ Invalid choice! Please try again.")


# Run the program
main()
