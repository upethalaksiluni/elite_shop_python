products = []
cart_items = []
VAT = 0.18  # 18% VAT


# Utility Functions (must be defined first)


# Product Module Functions
def add_products(product_id, name, price, quantity=0, description=""):
    """Add a product to the store with enhanced fields"""
    try:
        # Check if product ID already exists
        for product in products:
            if product["id"] == str(product_id):
                print(f"Product ID {product_id} already exists!")
                return False

        product = {
            "id": str(product_id),
            "name": name,
            "price": float(price),
            "quantity": int(quantity),
            "description": description
        }
        products.append(product)
        print(f"Product '{name}' added successfully!")
        return True
    except Exception as e:
        print(f"Error adding product: {e}")
        return False


def remove_products(product_id):
    """Remove a product from the store"""
    try:
        for i, product in enumerate(products):
            if product["id"] == str(product_id):
                removed_product = products.pop(i)
                print(f"Product '{removed_product['name']}' removed successfully!")
                return True
        print(f"Product with ID {product_id} not found!")
        return False
    except Exception as e:
        print(f"Error removing product: {e}")
        return False


def view_products():
    """Display all products in the store with enhanced information"""
    try:
        if not products:
            print("No products available in the store.")
            return

        print("\n=== ELITE SUPER STORE PRODUCTS ===")
        print(f"{'ID':<5} {'Name':<20} {'Price':<10} {'Stock':<8} {'Description':<30}")
        print("-" * 75)
        for product in products:
            description = product['description'][:27] + "..." if len(product['description']) > 30 else product[
                'description']
            print(
                f"{product['id']:<5} {product['name']:<20} ${product['price']:<9.2f} {product['quantity']:<8} {description:<30}")
        print()
    except Exception as e:
        print(f"Error viewing products: {e}")


def find_products_by_id(product_id):
    """Find and return a product by its ID"""
    try:
        for product in products:
            if product["id"] == str(product_id):
                return product
        return None
    except Exception as e:
        print(f"Error finding product: {e}")
        return None


def update_product_stock(product_id, new_quantity):
    """Update product stock quantity"""
    try:
        product = find_products_by_id(product_id)
        if product:
            product["quantity"] = int(new_quantity)
            print(f"Stock updated for '{product['name']}' to {new_quantity} units")
            return True
        else:
            print(f"Product with ID {product_id} not found!")
            return False
    except Exception as e:
        print(f"Error updating stock: {e}")
        return False
