def concatenate_lists(*args):
    combined = [item for lst in args for item in lst]
    return sorted(list(set(combined)))

list1 = [1, 2, 3]
list2 = [3, 4, 5]
list3 = [5, 6, 1]
result = concatenate_lists(list1, list2, list3)
print(result)

list4 = []
list5 = [1, 1, 1]
result2 = concatenate_lists(list4, list5)
print(result2) 