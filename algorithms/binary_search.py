"""
Бинарный поиск - алгоритм поиска со сложностью O(log n).
На вход: отсортированный список элементов.
На выходе: Позиция искомого элемента, иначе None.
"""
from support.decorators import timer


@timer
def binary_search(array, desired_item):
    left = 0
    right = len(array) - 1

    while left <= right:
        position = (left + right) // 2
        current_item = array[position]
        if current_item == desired_item:
            return position
        if current_item > desired_item:
            right = position - 1
        else:
            left = position + 1
    return None


if __name__ == "__main__":
    pass
