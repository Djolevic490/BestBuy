class Product:
    """Represents a product in the store with a name, price and quantity."""

    def __init__(self, name, price, quantity):
        # Check if the inputs are valid
        if name == "":
            raise Exception("Name must not be empty.")
        if price < 0:
            raise Exception("Price must not be negative.")
        if quantity < 0:
            raise Exception("Quantity must not be negative.")

        # Set the instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        # When the quantity reaches 0, the product is deactivated
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(self.name + ", Price: " + str(self.price) + ", Quantity: " + str(self.quantity))

    def buy(self, quantity):
        # Raise an exception if there is a problem
        if quantity <= 0:
            raise Exception("The purchase quantity must be greater than 0.")
        if quantity > self.quantity:
            raise Exception("There are not enough products in stock.")

        # Calculate the total price
        total_price = self.price * quantity

        # Update the quantity in stock
        self.set_quantity(self.quantity - quantity)

        return total_price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()
