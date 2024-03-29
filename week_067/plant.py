"""
Write a Plant class, for a garden simulation
A Plant knows: name, height and growth rate
When we water a plant, it grows according to:
    height += water * growth rate
"""


class Plant:
    def __init__(self, name="", height=0.0, growth_rate=0.0):
        self.name = name
        self.height = height
        self.growth_rate = growth_rate

    def __str__(self):
        return "{},{},{}".format(self.name, self.height, self.growth_rate)

    def water(self, water):
        self.height += water * self.growth_rate


p = Plant("Pigeon Pea", 1.0, 1.4)
print(p)
p.water(10)
print(p)

