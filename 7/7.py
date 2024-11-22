"""
Graph: Класс для представления графа. Содержит список рёбер.
add_edge: Метод для добавления ребра между двумя вершинами.
bellman_ford: Основной алгоритм:
Инициализация: Устанавливаем начальные расстояния.
Relaxation: Повторяем для всех рёбер 
V − 1
V − 1 раз.
Проверка на отрицательные циклы: Если после 
V − 1
V−1 итерации ещё можно уменьшить расстояния, значит, граф содержит отрицательный цикл.
Пример графа: Используется граф с 5 вершинами и несколькими рёбрами.
Вывод программы будет содержать либо кратчайшие расстояния, либо предупреждение о наличии отрицательного цикла.class Graph:
    """
    

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.edges = []    # Список рёбер графа

    def add_edge(self, u, v, weight):
        """Добавление ребра в граф"""
        self.edges.append((u, v, weight))

    def bellman_ford(self, src):
        """Алгоритм Беллмана-Форда"""
        # Инициализация расстояний до всех вершин
        distances = [9999999999.9] * self.V
        distances[src] = 0  # Расстояние до начальной вершины равно 0

        # Повторяем V-1 раз
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distances[u] != 9999999999.9 and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Проверка на наличие отрицательного цикла
        for u, v, weight in self.edges:
            if distances[u] != 9999999999.9 and distances[u] + weight < distances[v]:
                print("Граф содержит отрицательный цикл")
                return None

        return distances


# Пример использования
g = Graph(5)  # Создаём граф с 5 вершинами
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

# Запуск алгоритма Беллмана-Форда
source = 0
result = g.bellman_ford(source)

if result:
    print(f"Кратчайшие расстояния от вершины {source}: {result}")
