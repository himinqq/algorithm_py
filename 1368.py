import sys

input = sys.stdin.readline


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


N = int(input())

parent = [0] * (N+1)
for i in range(1,N+1):
    parent[i] = i

edges = []
# 우물 파는 비용을 간선으로 변환하여 추가
# 가상의 정점 (0번)에서 각 논(1~N번)으로 연결되는 간선
for i in range(1, N + 1):
    cost = int(input())
    edges.append((cost, 0, i))

# 논과 논을 잇는 간선
for i in range(1, N + 1):
    cost = list(map(int, input().split()))
    for j in range(1, N + 1):
        if i != j:
            edges.append((cost[j-1], i, j))

# 크루스칼 알고리즘
edges.sort()
total_cost = 0
edge_cnt = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        total_cost += cost
        if edge_cnt == N:
            break

print(total_cost)
