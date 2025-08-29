from product.product import cart_items, find_products_by_id


def add_to_cart(product_id, quantity=1):
    """Add a product to the cart"""
    try:
        product = find_products_by_id(product_id)
        if not product:
            print(f"Product with ID {product_id} not found!")
            return False

        if product["quantity"] < quantity:
            print(f"Sorry! Only {product['quantity']} units of '{product['name']}' available in stock.")
            return False

        for cart_item in cart_items:
            if cart_item["id"] == str(product_id):
                if product["quantity"] < (cart_item["quantity"] + quantity):
                    print(
                        f"Cannot add {quantity} more. Only {product['quantity']} total available, {cart_item['quantity']} already in cart.")
                    return False
                cart_item["quantity"] += int(quantity)
                print(f"Updated quantity for '{product['name']}' in cart!")
                return True

        cart_item = {
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": int(quantity)
        }
        cart_items.append(cart_item)
        print(f"'{product['name']}' added to cart!")
        return True
    except Exception as e:
        print(f"Error adding to cart: {e}")
        return False


def view_cart():
    """Display all items in the cart"""
    try:
        if not cart_items:
            print("Your cart is empty.")
            return

        print("\n=== YOUR CART ===")
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Qty':<5} {'Total':<10}")
        print("-" * 50)
        subtotal = 0
        for item in cart_items:
            item_total = item["price"] * item["quantity"]
            subtotal += item_total
            print(
                f"{item['id']:<5} {item['name']:<20} ${item['price']:<9.2f} {item['quantity']:<5} ${item_total:<9.2f}")
        print("-" * 50)
        print(f"Subtotal: ${subtotal:.2f}")
        print()
    except Exception as e:
        print(f"Error viewing cart: {e}")


def remove_item(product_id):
    """Remove an item from the cart"""
    try:
        for i, item in enumerate(cart_items):
            if item["id"] == str(product_id):
                removed_item = cart_items.pop(i)
                print(f"'{removed_item['name']}' removed from cart!")
                return True
        print(f"Item with ID {product_id} not found in cart!")
        return False
    except Exception as e:
        print(f"Error removing item from cart: {e}")
        return False
