from math import sqrt
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16]


evens = list(filter(lambda x: x % 2 == 0, numbers))
above_five = list(filter(lambda x: x > 5, numbers))
perfect_squares = list(filter(lambda x: sqrt(x).is_integer(), numbers))

print(f"Pairs: {evens}")
print(f"Supérieurs à 5: {above_five}")
print(f"Carrés parfaits: {perfect_squares}")
