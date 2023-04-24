# def add(*args):
#     tot = 0
#     for arg in args:
#         tot += arg
#     return tot
#
#
# print(add(2, 3, 4, 5, 6))

def calculate(n, **kvargs):
    print(kvargs)
    # different syntax, the first one allows None as value
    n += kvargs.get('add')
    n *= kvargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kvarg):
        self.make = kvarg.get('make')
        self.model = kvarg.get('model')
        self.color = kvarg.get("color")

my_car = Car(make="Fiat", model='500')
print(my_car.color)
print(my_car.make)




