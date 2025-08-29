from bill.bill import checkout
from cart.cart import view_cart, remove_item, add_to_cart
from product.product import view_products, update_product_stock, cart_items, remove_products, add_products


def run_shop():
    """Main function to run the store"""
    print("Welcome to Elite Super Store!")

    # Add some sample products with enhanced fields
    add_products("001", "Carrot", 100.00, 50, "Fresh organic carrots, locally sourced")
    add_products("002", "Apple", 50.00, 30, "Crispy red apples, perfect for snacking")
    add_products("003", "Banana", 30.00, 25, "Ripe yellow bananas, rich in potassium")
    add_products("004", "Orange", 75.00, 40, "Juicy Valencia oranges, vitamin C packed")
    add_products("005", "Milk", 120.00, 20, "Fresh whole milk, 1L bottle")

    while True:
        print("\n=== ELITE SUPER STORE MENU ===")
        print("1. View Products")
        print("2. Add Product to Store")
        print("3. Remove Product from Store")
        print("4. Add Product to Cart")
        print("5. View Cart")
        print("6. Remove Item from Cart")
        print("7. Checkout")
        print("8. Update Product Stock")
        print("9. Exit")

        try:
            choice = input("\nEnter your choice (1-9): ").strip()

            if choice == "1":
                view_products()

            elif choice == "2":
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                price = float(input("Enter product price: $"))
                quantity = int(input("Enter initial stock quantity: "))
                description = input("Enter product description: ")
                add_products(product_id, name, price, quantity, description)

            elif choice == "3":
                product_id = input("Enter product ID to remove: ")
                remove_products(product_id)

            elif choice == "4":
                view_products()
                product_id = input("Enter product ID to add to cart: ")
                quantity = int(input("Enter quantity (default 1): ") or "1")
                add_to_cart(product_id, quantity)

            elif choice == "5":
                view_cart()

            elif choice == "6":
                view_cart()
                if cart_items:  # Only ask for removal if cart has items
                    product_id = input("Enter product ID to remove from cart: ")
                    remove_item(product_id)

            elif choice == "7":
                view_cart()
                if cart_items:  # Only proceed if cart has items
                    confirm = input("Proceed to checkout? (y/n): ").lower()
                    if confirm == 'y':
                        checkout()

            elif choice == "8":
                view_products()
                product_id = input("Enter product ID to update stock: ")
                new_quantity = int(input("Enter new stock quantity: "))
                update_product_stock(product_id, new_quantity)

            elif choice == "9":
                print("Thank you for visiting Elite Super Store!")
                break

            else:
                print("Invalid choice! Please enter 1-9.")

        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


# Run the store if this file is executed directly
if __name__ == "__main__":
    run_shop()