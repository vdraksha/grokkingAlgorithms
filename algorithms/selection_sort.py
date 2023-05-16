"""Сортировка выбором - алгоритм сортировки со сложностью О(n^2)"""
from support.decorators import timer


@timer
def selection_sort(array):
    if len(array) < 2:
        return array
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array


def find_min(array, i, min_index):
    if i == len(array):
        return min_index
    if array[i] < array[min_index]:
        return find_min(array, i+1, i)
    return find_min(array, i+1, min_index)


@timer
def selection_sort_recursive(array, i=0):
    if len(array) < 2:
        return array
    if i == len(array) - 1:
        return array

    min_index = find_min(array, i+1, i)

    if min_index != i:
        array[i], array[min_index] = array[min_index], array[i]
    return selection_sort_recursive(array, i+1)


if __name__ == '__main__':
    pass
