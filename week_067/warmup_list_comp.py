"""
Write a list comprehension to produce a new list
containing only the products that are on sale
(True means a product is on sale)
"""


class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = ""
        if self.is_on_sale:
            on_sale_string = " (on sale!) :) #programmingisfun"
        return "{} ${:.2f}{}".format(self.name, self.price, on_sale_string)

    def __repr__(self):
        return str(self)


p = Product("Phone", 340)
print(p)
p2 = Product("PC", 1420.95, True)
print(p2)

INDEX_ON_SALE = 2

products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]
on_sale_products = [product for product in products if product.is_on_sale]
print(on_sale_products)

# products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
# on_sale_products = [product[0] for product in products if product[INDEX_ON_SALE]]
# print(on_sale_products)
