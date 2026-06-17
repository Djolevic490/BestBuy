import products
import store


def start(store_object):
    while True:
        # Show the menu
        print("")
        print("   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print("")
        choice = input("Please choose a number: ")

        if choice == "1":
            # List all products
            all_products = store_object.get_all_products()
            for product in all_products:
                product.show()

        elif choice == "2":
            # Show the total quantity in the store
            total = store_object.get_total_quantity()
            print("Total of " + str(total) + " items in store")

        elif choice == "3":
            # Collect items for the order
            all_products = store_object.get_all_products()
            for number in range(len(all_products)):
                # Show each product with its number, starting at 1
                print(str(number + 1) + ". ", end="")
                all_products[number].show()

            shopping_list = []
            print("When you want to finish order, enter empty text.")
            while True:
                product_choice = input("Which product # do you want? ")
                if product_choice == "":
                    break
                amount = input("What amount do you want? ")
                if amount == "":
                    break

                # Convert the text input into numbers
                product_index = int(product_choice) - 1
                amount = int(amount)
                chosen_product = all_products[product_index]
                shopping_list.append((chosen_product, amount))
                print("Product added to list!")

            if len(shopping_list) > 0:
                total_price = store_object.order(shopping_list)
                print("Order made! Total payment: $" + str(total_price))

        elif choice == "4":
            # Quit the program
            break

        else:
            print("Please choose a number from 1 to 4.")


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()
