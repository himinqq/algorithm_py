import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한대

# 노드개수, 간선 개수
n,m = map(int,input().split())
# 시작 노드 번호
start = int(input())

# 각 노드에 연결된 노드에 대한 정보
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c)) #a번 노드에서 b노드로 가는 비용 c

def dijkstra(start):
    q = []

    # 시작 노드 최단 경로 0로 초기화
    # heapq는 튜플의 첫 번째 값을 기준으로 최소값 먼저 꺼냄
    # 가장 짧은 거리부터 처리하기 위해 (거리, 노드번호) 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0

    # 큐가 빌때까지
    while q:
        # 가장 최단 거리 짧은 노드에 대한 정보 꺼내기
        cur_dist, node = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드면 무시
        if distance[node] < cur_dist:
            continue
        # 현재 노드와 인접한 다른 노드 확인
        for adj in graph[node]:
            # cost = 시작 → 현재 노드 → 인접 노드까지의 총 거리
            # dist=현재 노드까지 비용 + i[1]=현재노드에서 인접노드까지 비용
            cost = cur_dist + adj[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 테이블 업데이트
            if cost < distance[adj[0]]:
               heapq.heappush(q,(cost,adj[0]))
               distance[adj[0]] = cost

# 다익스트라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    if distance[i] == INF: #도달할 수 없는 경우 무한 출력
        print("INFINITY")
    else:
        print(distance[i]) #도달할 수 있는 경우 거리 출력