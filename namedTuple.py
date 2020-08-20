# Using namedtuple is way shorter than defining a class manually, how ?...:

from collections import namedtuple

Car = namedtuple('Car', 'color mileage size')

# "Car" class works as below..
my_car = Car('red', 3812.4, 10)

# Get a nice string repr for free:
print(my_car)

print(my_car.color)
print(my_car.mileage, '-', my_car.size)


# Like tuples, namedtuples are immutable
