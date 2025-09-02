import sys
input = sys.stdin.readline

N,M = map(int,input().split())
parent = [i for i in range(N+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
total_cost = 0
last_edge = 0

for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
edges.sort()

# 전체 신장 트리에서 가장 긴 간선 제거
# > 2개의 신장트리로 나뉨

for edge in edges:
    c,a,b = edge
    if find(a) != find(b):
        union(a, b)
        total_cost += c
        last_edge = c

print(total_cost-last_edge)
