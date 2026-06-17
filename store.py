import products


class Store:
    """Holds a list of products and lets the user buy several of them at once."""

    def __init__(self, product_list):
        # Save the list of products that the store contains
        self.products = product_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        # Add up the quantity of every product in the store
        total = 0
        for product in self.products:
            total = total + product.get_quantity()
        return total

    def get_all_products(self):
        # Return only the products that are active
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        # shopping_list is a list of tuples: (product, quantity)
        total_price = 0
        for item in shopping_list:
            product = item[0]
            quantity = item[1]
            total_price = total_price + product.buy(quantity)
        return total_price


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    all_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    if len(all_products) > 0:
        print(best_buy.order([(all_products[0], 1), (all_products[1], 2)]))
    else:
        print("No products available.")


if __name__ == "__main__":
    main()
