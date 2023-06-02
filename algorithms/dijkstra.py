"""Алгоритм Дейкстры - алгоритм поиска кратчайшего пути во взвешенном нецикличном графе с положительными весами.
Сложность алгоритма составляет O(n*n).
"""
from support.decorators import timer


def collect_path(routes, start_node, desired_node):
    node = routes[desired_node]
    result = [node[1], desired_node, node[0]]
    while node[0] != start_node:
        node = routes[node[0]]
        result.append(node[0])
    return result[::-1]


@timer
def find_path(graph, start_node, desired_node):
    visited = []
    routes = {start_node: (None, 0)}
    queue = [start_node]

    if start_node == desired_node:
        return f"Уже находимся в {start_node}."

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node not in graph:   # Если узел не имеет потомком
                continue
            cost = routes[node][1]  # Берем стоимость пути до старого узла
            for child in graph[node]:
                new_cost = cost + child[1]  # Считаем стоимость пути до нового узла от старого
                if child[0] in routes:
                    old_cost = routes[child[0]][1]  # Берем стоимость существующего пути до нового узла
                    if old_cost > new_cost:
                        routes[child[0]] = (node, new_cost)
                else:
                    routes[child[0]] = (node, new_cost)
                queue.append(child[0])

    if desired_node not in routes:
        return f"Пути из {start_node} в {desired_node} не существует."
    else:
        return collect_path(routes, start_node, desired_node)


if __name__ == "__main__":
    g = {
        "A": [("B", 5), ("C", 2)],
        "B": [("D", 4), ("E", 2)],
        "C": [("B", 8), ("E", 7)],
        "D": [("F", 3), ("E", 6)],
        "E": [("F", 1)]
    }
    print(find_path(g, "A", "F"))   # ['A', 'B', 'E', 'F', 8]
    print(find_path(g, "F", "A"))   # Пути из F в A не существует.
    print(find_path(g, "B", "F"))   # ['B', 'E', 'F', 3]
    print(find_path(g, "A", "A"))   # Уже находимся в A.
