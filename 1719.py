import sys

input = sys.stdin.readline
N, M = map(int, input().split())
INF = float('inf')
graph = [[INF] * (N + 1) for _ in range(N + 1)]
dist = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    dist[a][b] = b
    dist[b][a] = a

for i in range(1, N + 1):
    graph[i][i] = 0
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                dist[a][b] = dist[a][k]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            print("-",end=" ")
        else:
            print(dist[i][j], end=" ")
    print()