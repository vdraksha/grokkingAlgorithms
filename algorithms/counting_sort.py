"""Сортировка подсчетом - алгоритм сортировки со сложностью О(n) в лучшем и среднем, и O(n^2) в худшем случае"""
from support.decorators import timer


@timer
def counting_sort(array, max_item, min_item):
    count = [0] * (max_item + 1)
    j = 0
    for item in array:
        count[item] += 1
    for i in range(min_item, max_item + 1, 1):
        while count[i] > 0:
            array[j] = i
            count[i] -= 1
            j += 1
    return array


if __name__ == "__main__":
    pass


