class Graph:
    def __init__(self, size):
        self.adjMatrix = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size

    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1

    def topo_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in range(self.size):
            if self.adjMatrix[v][i] == 1 and not visited[i]:
                self.topo_sort_util(i, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = [False] * self.size
        stack = []
        for i in range(self.size):
            if not visited[i]:
                self.topo_sort_util(i, visited, stack)
        return stack

    def count_paths(self, v, u):
        order = self.topological_sort()
        paths = [0] * self.size
        paths[v] = 1  # путь от v к v за 1

        for node in order:
            for i in range(self.size):
                if self.adjMatrix[node][i] == 1:
                    paths[i] += paths[node]

        return paths[u]

# пример
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

v, u = 0, 4
print(f"Количество путей от {v} до {u}: {g.count_paths(v, u)}")
