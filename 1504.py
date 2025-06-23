import heapq

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
INF = int(1e9)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


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
            cost = curr_dist + adj[1]
            if cost < dist[adj[0]]:
                dist[adj[0]] = cost
                heapq.heappush(q, (cost, adj[0]))
    return dist


v1, v2 = map(int, input().split())
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 경로 1: 1 -> v1 -> v2 -> N
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
# 경로 2: 1 -> v2 -> v1 -> N
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]
result = min(path1, path2)
print(result if result < INF else -1)
