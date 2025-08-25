# id, name, price, quantity

product_id = []
product_name = []
product_price = []
product_quantity = []
product_description = []


def add_products():
    while True:

        id = int(input("enter a id : "))
        name = input("Enter a product name : ")
        price = input("Enter a product price : ")
        quantity = int(input("Enter a product quantity : "))
        description = input("Enter a product description : ")

        product_id.append(id)
        product_name.append(name)
        product_price.append(price)
        product_quantity.append(quantity)
        product_description.append(description)

        con = input("if you want to add product press 'Y' : ")

        if con == "N":
            break


def remove_product():
    remove_products = int(input("Enter a id for remove product : "))

    product_id.pop(remove_products - 1)
    product_name.append(remove_products - 1)
    product_price.append(remove_products - 1)
    product_quantity.append(remove_products - 1)
    product_description.append(remove_products - 1)


def view_products():
    lenth = int(len(product_id))
    for pro_count in range(lenth):
        print(
            f"product id is = {product_id[pro_count]} product name is = {product_name[pro_count]} product price is = {product_price[pro_count]} product quantity is = {product_quantity[pro_count]}  product description is = {product_description[pro_count]} ")


def find_product_by_id(p_id):
    if p_id in product_id:
        index = product_id.index(p_id)
        print(f"Product id: {product_id[p_id - 1]} \n "
              f"Product Name: {product_name[p_id - 1]} \n "
              f"Product Price: {product_price[p_id - 1]} \n"
              f"Product Description: {product_description[p_id - 1]}")
    else:
        print("Product not found. Please Try again!!! :(")
