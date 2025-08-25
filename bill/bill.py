import cart.cart


def calculate_bill():
    sub_total = sum([Item["price"] for item in
                     cart.cart.cart_items])
    vat = 0.18
    vat_amount = sub_total * vat
    total = sub_total + vat_amount
    return {
        "Sub Total: " : sub_total,
        "VAT Amount: ": vat_amount,
        "Final Total: ": total
    }

def chekout():
    bill = calculate_bill()
    cart.cart_items.clear()
    return bill