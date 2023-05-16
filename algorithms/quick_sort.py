"""Быстрая сортировка - алгоритм сортировки со сложностью О(n^2) в худшем и O(n*log(n)) в среднем и лучшем случае"""
from support.decorators import timer


@timer
def quick_sort_recursive(array):
    if len(array) < 2:
        return array
    pivot = array[len(array)//2]    # Опорный элемент может быть array[0], серединным и медианным(см. разбиение Ломуто)
    max_arr = [i for i in array if i > pivot]
    piv_arr = [i for i in array if i == pivot]
    min_arr = [i for i in array if i < pivot]
    return quick_sort_recursive(min_arr) + piv_arr + quick_sort_recursive(max_arr)


if __name__ == "__main__":
    pass
