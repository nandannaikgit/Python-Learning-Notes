# -----------------------------
# CLASS 1: PRODUCT
# -----------------------------
class Product:
    def __init__(self, pid, name, price, stock, discount=0):
        self.pid = pid
        self.name = name
        self.price = price
        self.stock = stock
        self.discount = discount  # discount in %

    def get_price_after_discount(self):
        return self.price - (self.price * self.discount / 100)


# -----------------------------
# CLASS 2: INVENTORY
# -----------------------------
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.pid] = product

    def show_products(self):
        print("\n--- Available Products ---")
        for p in self.products.values():
            price = p.get_price_after_discount()
            print(f"{p.pid}. {p.name} - ₹{price}  (Stock: {p.stock}) Discount: {p.discount}%")
        print("--------------------------")

    def get_product(self, pid):
        return self.products.get(pid, None)


# -----------------------------
# CLASS 3: CART
# -----------------------------
class Cart:
    def __init__(self):
        self.items = {}  # pid: qty

    def add_to_cart(self, product, qty):
        if product.stock < qty:
            print("❌ Not enough stock!")
            return

        if product.pid in self.items:
            self.items[product.pid] += qty
        else:
            self.items[product.pid] = qty

        product.stock -= qty
        print(f"✔ Added {qty} x {product.name} to cart")

    def remove_from_cart(self, product):
        if product.pid not in self.items:
            print("❌ Item not in cart!")
            return

        product.stock += self.items[product.pid]
        del self.items[product.pid]
        print(f"✔ Removed {product.name} from cart")

    def calculate_subtotal(self, inventory):
        total = 0
        for pid, qty in self.items.items():
            product = inventory.get_product(pid)
            total += product.get_price_after_discount() * qty
        return total


# -----------------------------
# CLASS 4: ORDER
# -----------------------------
class Order:
    TAX_RATE = 0.18  # 18% GST
    SHIPPING_RATE = 40  # Flat shipping

    def __init__(self, cart, inventory):
        self.cart = cart
        self.inventory = inventory
        self.status = "Pending"

    def calculate_total(self):
        subtotal = self.cart.calculate_subtotal(self.inventory)
        tax = subtotal * Order.TAX_RATE
        shipping = Order.SHIPPING_RATE if subtotal < 500 else 0  # free shipping above ₹500
        grand_total = subtotal + tax + shipping
        return subtotal, tax, shipping, grand_total

    def place_order(self):
        self.status = "Completed"
        print("\n🛒 Order Placed Successfully!")
        print(f"Order Status: {self.status}")


# -----------------------------
# CLASS 5: CUSTOMER (For future expansion)
# -----------------------------
class Customer:
    def __init__(self, name):
        self.name = name


# -----------------------------
# MAIN APPLICATION
# -----------------------------
def main():
    # Setup
    inventory = Inventory()
    inventory.add_product(Product(1, "Laptop", 50000, 5, discount=10))
    inventory.add_product(Product(2, "Headphones", 2000, 10, discount=5))
    inventory.add_product(Product(3, "Smartphone", 35000, 7))
    inventory.add_product(Product(4, "Keyboard", 80, 15, discount=20))

    cart = Cart()
    customer = Customer("Nandan")

    while True:
        print("\n===== E-Commerce Menu =====")
        print("1. Browse Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            inventory.show_products()

        elif choice == "2":
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity: "))
            product = inventory.get_product(pid)
            if product:
                cart.add_to_cart(product, qty)
            else:
                print("❌ Invalid Product ID")

        elif choice == "3":
            pid = int(input("Enter Product ID to remove: "))
            product = inventory.get_product(pid)
            if product:
                cart.remove_from_cart(product)
            else:
                print("❌ Invalid Product ID")

        elif choice == "4":
            order = Order(cart, inventory)
            subtotal, tax, shipping, total = order.calculate_total()

            print("\n===== Billing Summary =====")
            print(f"Subtotal: ₹{subtotal}")
            print(f"GST (18%): ₹{tax}")
            print(f"Shipping: ₹{shipping}")
            print(f"Total Amount: ₹{total}")
            print("===========================")

            confirm = input("Place Order? (yes/no): ").lower()
            if confirm == "yes":
                order.place_order()
                break

        elif choice == "5":
            print("Thank you for shopping with us! 😊")
            break

        else:
            print("❌ Invalid choice!")


main()
