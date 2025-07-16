import heapq
import sys

input = sys.stdin.readline

n, m, start, end, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

INF = float('inf')


def dijkstra(limit):
    dist = [INF] * (n + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        cost, now = heapq.heappop(q)
        if now == end:
            return True
        if dist[now] < cost:
            continue
        for nxt, w in graph[now]:
            new_cost = cost + w
            if w > limit:
                continue  # 임계값 초과한 간선은 무시
            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heapq.heappush(q, (dist[nxt], nxt))
    return False


# 이분 탐색
left, right = 0, 1_000_000_000
ans = -1
while left <= right:
    mid = (left + right) // 2
    if dijkstra(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans if ans <= c else -1)
