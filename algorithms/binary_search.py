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


@timer
def binary_search_recursive(array, desired_item, left=0, right=None):
    if not right:
        right = len(array) - 1
    if left > right:
        return False

    position = (left + right) // 2
    if desired_item == array[position]:
        return position
    elif array[position] > desired_item:
        return binary_search_recursive(array, desired_item, left, position-1)
    return binary_search_recursive(array, desired_item, position+1, right)


if __name__ == "__main__":
    pass

