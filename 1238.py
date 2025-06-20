# 학생, 도로, 마을
import heapq

n, m, x = map(int, input().split())

INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    dist = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        curr_dist, node = heapq.heappop(q)

        if dist[node] < curr_dist:
            continue

        for adj in graph[node]:
            cost = adj[1] + curr_dist
            if cost < dist[adj[0]]:
                dist[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))
    return dist

dist_from_x = dijkstra(x)

max_time = 0
for i in range(1,n+1):
    dist_to_x = dijkstra(i)
    total_time = dist_to_x[x] + dist_from_x[i]
    max_time = max(total_time,max_time)

print(max_time)

