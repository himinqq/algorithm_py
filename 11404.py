import sys
input = sys.stdin.readline

city_n = int(input())
bus_m = int(input())

INF = int(1e9)
graph = [[INF] * (city_n + 1) for _ in range(city_n + 1)]

for a in range(1, city_n+1):
    for b in range(1, city_n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(bus_m):
    a, b, c = map(int, input().split())
    if graph[a][b] == INF:
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)

for k in range(1, city_n+1):
    for a in range(1, city_n+1):
        for b in range(1, city_n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, city_n+1):
    for b in range(1, city_n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
