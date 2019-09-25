from collections import OrderedDict


# d = {1: 2}
# print(type(d))
# od = OrderedDict()


class Thing:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return self.x < other.x

    def __add__(self, other):
        return Thing(self.x + other.x)

    def one(self):
        print('VERY IMPORTANT'.title())

    def do_thing(self):
        print('do thing')


class SpecialThing(Thing):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def one(self):
        super().one()
        # print('VERY IMPORTANT')
        print("special one")

    def two(self):
        print("two")


t = Thing(1)
# t.one()
# Thing.one(t)
# t.do_thing()
# t.two()

st = SpecialThing(2, 3)
# st.one()
# st.do_thing()
# st.two()

t2 = Thing(2)
t + t
print(t == st)
print(t < st)
print(st.__lt__(t))
