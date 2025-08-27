from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    # 지도 정보 이용하여 최단시간에 부대로 복귀하기
    # src 원소 순서대로 복귀할 수 있는 최단시간 담은 배열 리턴
    # 복귀 불가능한 경우 -1 리턴

    INF = -1

    graph = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # 모든 노드간 거리1 이므로 힙 사용할 필요 없음 (순서대로 최단거리)
    q = deque([destination])
    dist[destination] = 0
    while q:
        node = q.popleft()
        for adj in graph[node]:
            if dist[adj] == INF:
                q.append(adj)
                dist[adj] = dist[node] + 1

    return [dist[src] for src in sources]