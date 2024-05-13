### 1. Максимальный среди весов используемых рёбер

def dijkstra_max_edge(n, edges, start):
    inf = float('inf')
    dist = [inf] * n
    dist[start] = 0
    heap = [(0, start)]  # (max_weight, node)
    
    while heap:
        cost, u = min(heap)
        heap.remove((cost, u))
        for v, weight in edges[u]:
            max_edge = max(cost, weight)
            if max_edge < dist[v]:
                dist[v] = max_edge
                heap.append((max_edge, v))
    
    return dist

# Примерчик
n = 5
edges = {
    0: [(1, 5), (2, 2)],
    1: [(3, 1)],
    2: [(3, 4)],
    3: [(4, 3)],
    4: []
}
print(dijkstra_max_edge(n, edges, 0))


### 2. Произведение весов рёбер

def dijkstra_product_edge(n, edges, start):
    inf = float('inf')
    dist = [inf] * n
    dist[start] = 1
    heap = [(1, start)]  # (product, node)
    
    while heap:
        cost, u = min(heap)
        heap.remove((cost, u))
        for v, weight in edges[u]:
            product = cost * weight
            if product < dist[v]:
                dist[v] = product
                heap.append((product, v))
    
    return dist

# Примерчик
n = 5
edges = {
    0: [(1, 5), (2, 2)],
    1: [(3, 1)],
    2: [(3, 4)],
    3: [(4, 3)],
    4: []
}
print(dijkstra_product_edge(n, edges, 0))


### 3. Конкатенация строк, написанных на рёбрах

def dijkstra_concat_strings(n, edges, start):
    inf = ""
    dist = [inf] * n
    dist[start] = ""
    heap = [(len(dist[start]), start)]  # (length of path, node)
    
    while heap:
        cost, u = min(heap)
        heap.remove((cost, u))
        for v, weight_str in edges[u]:
            new_path = dist[u] + weight_str
            if dist[v] == "" or len(new_path) < len(dist[v]):
                dist[v] = new_path
                heap.append((len(new_path), v))
    
    return dist

# Примерчик
n = 5
edges = {
    0: [(1, "a"), (2, "bc")],
    1: [(3, "d")],
    2: [(3, "ef")],
    3: [(4, "gh")],
    4: []
}
print(dijkstra_concat_strings(n, edges, 0))

### 4. Минимальный среди весов используемых рёбер с максимизацией стоимости пути

def dijkstra_min_edge_max(n, edges, start):
    inf = float('-inf')
    dist = [inf] * n
    dist[start] = float('inf')
    heap = [(-dist[start], start)]  # (negative min_edge, node)
    
    while heap:
        cost, u = max(heap)
        heap.remove((cost, u))
        cost = -cost
        for v, weight in edges[u]:
            min_edge = min(cost, weight)
            if min_edge > dist[v]:
                dist[v] = min_edge
                heap.append((-min_edge, v))
    
    return dist

# Примерчик
n = 5
edges = {
    0: [(1, 5), (2, 2)],
    1: [(3, 3)],
    2: [(3, 4)],
    3: [(4, 1)],
    4: []
}
print(dijkstra_min_edge_max(n, edges, 0))

### 5. Минимизация количества смен цвета узлов вдоль пути

def dijkstra_min_color_changes(n, edges, colors, start):
    inf = float('inf')
    dist = [(inf, inf)] * n  # (color_changes, total_cost)
    dist[start] = (0, 0)
    heap = [(0, 0, start)]  # (color_changes, total_cost, node)
    
    while heap:
        color_changes, cost, u = min(heap)
        heap.remove((color_changes, cost, u))
        for v, weight in edges[u]:
            new_color_changes = color_changes + (1 if colors[u] != colors[v] else 0)
            new_cost = cost + weight
            if (new_color_changes, new_cost) < dist[v]:
                dist[v] = (new_color_changes, new_cost)
                heap.append((new_color_changes, new_cost, v))
    
    return dist

# Примерчик
n = 5
edges = {
    0: [(1, 5), (2, 2)],
    1: [(3, 1)],
    2: [(3, 4)],
    3: [(4, 3)],
    4: []
}
colors = [0, 1, 0, 1, 0]
print(dijkstra_min_color_changes(n, edges, colors, 0))


