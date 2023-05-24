"""Поиск в ширину - алгоритм поиска в графах со сложностью O(n+k), где n - количество вершин, k - количество ребер"""
from support.decorators import timer


@timer
def bf_search(graph, start_node, desired_node):
    visited = []
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            if node == desired_node:
                return f"Узел '{desired_node}' cуществует для узла '{start_node}'"
            else:
                visited.append(node)
                queue += graph[node]
    return f"Узел '{desired_node}' не cуществует для узла '{start_node}'"


if __name__ == "__main__":
    pass

