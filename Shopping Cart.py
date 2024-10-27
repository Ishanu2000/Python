#Represent a product with a name, price, and quantity
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

#Manage the shopping cart
class ShoppingCart:
    def __init__(self):
        #Dictionary to store products; keys are product names, values are Product instances
        self.cart = {}

    #Add a product to the cart
    def add_product(self, product):
        if product.name in self.cart:
            #If product already in cart, increase its quantity
            self.cart[product.name].quantity += product.quantity
        else:
            #Add new product to the cart
            self.cart[product.name] = product
        print(f"Added {product.quantity} of {product.name} to the cart.")

    #Remove a product from the cart
    def remove_product(self, product_name):
        if product_name in self.cart:
            removed_product = self.cart.pop(product_name)  # Remove the product
            print(f"\nRemoved {removed_product.name} from the cart.")
        else:
            print("Product not found in the cart.")

    #calculate the total price of items in the cart
    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.cart.values())
        return total

    #Display the contents of the cart
    def display_cart(self):
        if not self.cart:
            print("The cart is empty.")
        else:
            print("\n-----Shopping Cart Contents-----")
            for product in self.cart.values():
                print(f"{product.name} - Price: ${product.price}, Quantity: {product.quantity}")

#Example
#Create a ShoppingCart instance
shopping_cart = ShoppingCart()

#Create and add products to the cart
shopping_cart.add_product(Product("Apple", 0.5, 4))
shopping_cart.add_product(Product("Banana", 0.2, 10))
shopping_cart.add_product(Product("Orange", 0.8, 5))

#Display cart contents
shopping_cart.display_cart()

#Calculate and display the total price
total_price = shopping_cart.calculate_total()
print(f"Total Price: ${total_price:.2f}")

#Remove a product from the cart
shopping_cart.remove_product("Banana")

#Display cart contents again after removal
shopping_cart.display_cart()

#Calculate and display the new total price
total_price = shopping_cart.calculate_total()
print(f"Total Price: ${total_price:.2f}")
