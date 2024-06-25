list_1 = [*range(-9, 10)]
sorted(list_1)
print(list_1)


def squared_list(array: list[int]) -> list[int]:
    return [x**2 for x in array]


print(sorted(squared_list(list_1)))
