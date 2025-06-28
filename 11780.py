n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
nxt = [[0] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    nxt[a][b] = b

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                nxt[a][b] = nxt[a][k]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()


def reconstruct_path(start, end):  # 경로복원
    if nxt[start][end] == 0:
        return 0
    path = [start]
    while start != end:
        start = nxt[start][end]
        path.append(start)
    return path


for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF or a == b:
            print(0)
        else:
            path = reconstruct_path(a, b)
            print(len(path), *path)


