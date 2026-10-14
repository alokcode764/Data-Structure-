# Graph Traversals

from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}

print("Adjacency List:")
for v in graph:
    print(v, ":", graph[v])

matrix = [[0]*5 for _ in range(5)]
for u in graph:
    for v in graph[u]:
        matrix[u][v] = 1

print("\nAdjacency Matrix:")
for row in matrix:
    print(row)

def dfs(start):
    visited, stack, order = set(), [start], []
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            order.append(u)
            stack += graph[u][::-1]
    return order

def bfs(start):
    visited, q, order = {start}, deque([start]), []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order

print("\nDFS:", dfs(0))
print("BFS:", bfs(0))