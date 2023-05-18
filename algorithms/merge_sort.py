"""Сортировка слиянием - алгоритм сортировки со сложностью O(n*log(n))"""
from support.decorators import timer


def merge(left, right):
    array = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))
    if left:
        array = array + left
    if right:
        array = array + right
    return array


@timer
def merge_sort(array):
    if len(array) == 1:
        return array
    left = merge_sort(array[:len(array)//2])
    right = merge_sort(array[len(array)//2:])
    return merge(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    a = [3, 5, 1, 6, 9, 8, 2]
    print(merge_sort(a))

