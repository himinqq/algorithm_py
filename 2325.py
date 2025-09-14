import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = float('inf')

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 1에서 N까지 최단거리 찾기
def find_shortest():
    dist = [INF] * (N + 1)
    prev = [0] * (N + 1)
    dist[1] = 0
    q = [(0, 1)]
    while q:
        cost, node = heapq.heappop(q)
        if cost > dist[node]:
            continue
        for nxt, c in graph[node]:
            new_cost = cost + c
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                prev[nxt] = node
                heapq.heappush(q, (new_cost, nxt))

    path = [N]
    cur = N
    while cur != 1:
        cur = prev[cur]
        path.append(cur)
    path.reverse()
    return path

# 특정 간선 무시하는 다익스트라
def ignore_di(edge):
    dist = [INF] * (N + 1)
    dist[1] = 0
    q = [(0, 1)]
    while q:
        cost, node = heapq.heappop(q)
        if cost > dist[node]:
            continue
        for nxt, c in graph[node]:
            if (node, nxt) == edge or (nxt, node) == edge:
                continue
            new_cost = cost + c
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))
    return dist[N]

shortest = find_shortest()
ans = []
for i in range(len(shortest) - 1):
    edge = (shortest[i], shortest[i+1])
    ans.append(ignore_di(edge))

print(max(ans))
