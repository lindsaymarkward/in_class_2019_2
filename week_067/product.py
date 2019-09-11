"""Product class."""


class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = ""
        if self.is_on_sale:
            on_sale_string = " (on sale!)"
        return "{} ${:.2f}{}".format(self.name, self.price, on_sale_string)

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    print("I'm in product.py")
    products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]
    on_sale_products = [product for product in products if product.is_on_sale]
    print(on_sale_products)
