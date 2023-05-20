"""Поразрядная сортировка - алгоритм сортировки со сложностью O(n*k), где k - количество разрядов."""
from support.decorators import timer


@timer
def radix_sort(array, base):
    max_len = max([len(str(item)) for item in array])
    bins = [[] for _ in range(base)]

    for i in range(0, max_len, 1):
        for item in array:
            digit = (item // base ** i) % base
            bins[digit].append(item)
        array = [x for item in bins for x in item]
        bins = [[] for _ in range(base)]
    return array


if __name__ == '__main__':
    pass
