"""Product demo program.
Load products, display, add and put them on sale.
"""
from week_067.product import Product

MENU_STRING = "D.isplay products\nA.dd product\nP.ut product on sale"
FILENAME = "products.txt"


def main():
    products = load_products(FILENAME)
    print(MENU_STRING)
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "D":
            display_products(products)
        else:
            print("Invalid")
        print(MENU_STRING)
        choice = input("> ").upper()

    product = Product()
    print(product)


def display_products(products):
    for product in products:
        print(product)


def load_products(filename):
    products = []
    with open(filename) as input_file:
        for line in input_file:
            # print(repr(line))
            parts = line.strip().split(', ')
            # print(parts)
            is_on_sale = parts[2] == "on"
            product = Product(parts[0], float(parts[1]), is_on_sale)
            products.append(product)
            # print(product)
    return products


if __name__ == '__main__':
    main()
