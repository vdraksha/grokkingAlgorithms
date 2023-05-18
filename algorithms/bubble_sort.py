"""Пузырьковая сортировка - алгоритм сортировки со сложностью O(n^2)"""
from support.decorators import timer


@timer
def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(len(array)):
            if j == i:
                break
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
    return array


@timer
def bubble_sort_recursive(array, left=0, last=None):
    if last is None:
        last = len(array) - 1
    if left != last:
        if array[left] > array[last]:
            array[left], array[last] = array[last], array[left]
        return bubble_sort_recursive(array, left+1, last)
    if last > 0:
        return bubble_sort_recursive(array, 0, last-1)
    else:
        return array


if __name__ == '__main__':
    pass
