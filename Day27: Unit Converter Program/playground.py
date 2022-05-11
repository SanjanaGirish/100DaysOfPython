# Many Position Arguments
# def add(*args):
#     print(type(args))
#     return sum(args)
# print(add(3, 5, 6))
# print(add(21, -11, 6))

# Many Keyword Arguments
# def calculate(n, **kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
# calculate(2, add=5, multiply=3)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car( model="GT-R")
print(my_car.model)
print(my_car.make) # Default value is None as it isn't set
