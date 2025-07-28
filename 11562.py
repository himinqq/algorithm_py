import sys

input = sys.stdin.readline
N, M = map(int,input().split())
INF = float('inf')
graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u,v,b = map(int,input().split())
    if b == 0:
        graph[u][v] = 0
        graph[v][u] = 1
    else:
        graph[u][v] = 0
        graph[v][u] = 0

K = int(input())

for i in range(1,N+1):
    graph[i][i] = 0

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            if graph[a][k]+graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k]+graph[k][b]
for _ in range(K):
    s,e = map(int,input().split())
    print(graph[s][e])