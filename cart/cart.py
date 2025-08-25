cart_items = []


def add_to_cart(p_id):
    cart_items.append(p_id)


def view_cart():
    return cart_items


def remove_item(p_id):
    global cart_items
    cart_items = [p for p in cart_items if p["id"] != p_id]
