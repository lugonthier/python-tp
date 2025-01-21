from functools import reduce

numbers = [1, 2, 3, 4, 5]
strings = ['Hello', ' ', 'World', '!']

sum_result = reduce(lambda x, y: x + y, numbers)
max_result = reduce(lambda x, y: x if x > y else y, numbers)
concat_result = reduce(lambda x, y: x + y, strings)

print(f"Somme: {sum_result} (built-in: {sum(numbers)})")
print(f"Max: {max_result} (built-in: {max(numbers)})")
print(f"Concat: {concat_result}")
