# kruskal & prim :
edges = [(0,1,2),(0,2,3),(1,2,1),(1,3,4),(2,3,5)]


# Kruskal
parent = list(range(4))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

mst = []
for u,v,w in sorted(edges, key=lambda x:x[2]):
    a,b = find(u), find(v)
    if a != b:
        parent[a] = b
        mst.append((u,v,w))

print("Kruskal MST:", mst)
print("Cost:", sum(w for u,v,w in mst))

# Prim
g = {0:[(1,2),(2,3)], 1:[(0,2),(2,1),(3,4)],
     2:[(0,3),(1,1),(3,5)], 3:[(1,4),(2,5)]}

visited = {0}
mst = []

while len(visited) < 4:
    edge = min((w,u,v) for u in visited
               for v,w in g[u] if v not in visited)
    w,u,v = edge
    visited.add(v)
    mst.append((u,v,w))

print("\nPrim MST:", mst)
print("Cost:", sum(w for u,v,w in mst))