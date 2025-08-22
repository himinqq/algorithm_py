# 1번 노드에서 가장 멀리 떨어진 노드 찾기
import heapq


def solution(n, edge):
    answer = 0
    INF = float('inf')
    graph = [[] for _ in range(n+1)]

    for a,b in edge:
        graph[a].append([b,1])
        graph[b].append([a,1])


    dist = [INF] * (n+1)
    def dijkstra(v):
        q = []
        heapq.heappush(q,(0,v))
        dist[v] = 0
        while q:
            cost, node = heapq.heappop(q)
            if dist[node] < cost:
                continue
            for adj, adj_cost in graph[node]:
                new_cost = cost + adj_cost
                if new_cost < dist[adj]:
                    dist[adj] = new_cost
                    heapq.heappush(q,(new_cost,adj))
    dijkstra(1)
    max_dist = max(d for d in dist if d != INF)
    answer = dist.count(max_dist)

    return answer