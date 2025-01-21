numbers = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x * 2, numbers))
strings = list(map(lambda x: str(x), numbers))
squares = list(map(lambda x: x ** 2, numbers))

print(f"Doubles: {doubles}")
print(f"Strings: {strings}")
print(f"Squares: {squares}")
