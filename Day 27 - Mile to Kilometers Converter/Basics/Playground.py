def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
    return sum

add(3, 4, 5, 6)


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-R")
    