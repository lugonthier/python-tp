def apply_operations(data, operations):
    """
    Applique une série d'opérations sur chaque élément
    """
    result = data.copy()
    for op in operations:
        result = list(map(op, result))
    return result

double = lambda x: x * 2
add_one = lambda x: x + 1
square = lambda x: x ** 2

numbers = [1, 2, 3]
ops = [double, add_one, square]
result = apply_operations(numbers, ops)
print(f"Résultat: {result}")
