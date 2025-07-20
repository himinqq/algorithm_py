N = int(input())
INF = float('inf')
graph = [[INF]*(N+1) for _ in range(N+1)]

# 자기 자신까지의 거리는 0으로 초기화
for i in range(1, N + 1):
    graph[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_score = float('inf')
scores = [0] * (N + 1)
for i in range(1,N+1):
    scores[i] = max(graph[i][1:])
    min_score = min(min_score,scores[i])

candidates = []
for i in range(1,N+1):
    if scores[i] == min_score:
        candidates.append(i)
print(min_score,len(candidates))
print(*candidates)