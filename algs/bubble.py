our_list = [3, 5, 2, 7, 1, 4, 5, 6, 9, 8, 3]

length = len(our_list)
print(len(our_list))


def bubble_sort_for(array):
    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort_while(array):
    i = 0
    while i < length - 1:
        j = 0
        while j < length - i - 1:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1
    return array


print(1)
print(our_list)
print(bubble_sort_for(our_list[:]))
print(2)
print(our_list)
print(bubble_sort_while(our_list[:]))
