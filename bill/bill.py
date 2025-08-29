from product.product import cart_items, find_products_by_id, VAT


def calculate_bill():
    """Calculate the total bill including VAT"""
    try:
        if not cart_items:
            print("Cart is empty! Cannot calculate bill.")
            return 0

        subtotal = 0
        for item in cart_items:
            subtotal += item["price"] * item["quantity"]

        vat_amount = subtotal * VAT
        total = subtotal + vat_amount

        return {
            "subtotal": subtotal,
            "vat_amount": vat_amount,
            "total": total
        }
    except Exception as e:
        print(f"Error calculating bill: {e}")
        return 0


def checkout():
    """Process checkout and display final bill"""
    try:
        if not cart_items:
            print("Cart is empty! Cannot checkout.")
            return False

        bill = calculate_bill()
        if not bill:
            return False

        # Check stock availability before finalizing
        for item in cart_items:
            product = find_products_by_id(item["id"])
            if not product or product["quantity"] < item["quantity"]:
                print(f"Sorry! '{item['name']}' is out of stock or insufficient quantity available.")
                return False

        # Update stock quantities
        for item in cart_items:
            product = find_products_by_id(item["id"])
            product["quantity"] -= item["quantity"]

        print("\n" + "=" * 40)
        print("          ELITE SUPER STORE")
        print("             RECEIPT")
        print("=" * 40)
        for item in cart_items:
            item_total = item["price"] * item["quantity"]
            print(f"{item['name']:<20} {item['quantity']}x${item['price']:.2f} = ${item_total:.2f}")

        print("-" * 40)
        print(f"Subtotal: ${bill['subtotal']:.2f}")
        print(f"VAT ({VAT * 100}%): ${bill['vat_amount']:.2f}")
        print(f"TOTAL: ${bill['total']:.2f}")
        print("=" * 40)
        print("Thank you for shopping with us!")
        print("=" * 40)

        # Clear cart after successful checkout
        cart_items.clear()
        return True
    except Exception as e:
        print(f"Error during checkout: {e}")
        return False