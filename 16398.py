N = int(input())
edges = []
parent = [i for i in range(N + 1)]

for i in range(N):
    costs = list(map(int, input().split()))
    for j in range(N):
        if i != j:
            edges.append([costs[j], i + 1, j + 1])


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total_cost = 0
edge_cnt = 0
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        edge_cnt += 1
        total_cost += cost
        if edge_cnt == N - 1:
            break

print(total_cost)
