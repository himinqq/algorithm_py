import heapq

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(m)]
INF = float('inf')
dist = [[INF] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    q = []
    dist[0][0] = 0
    heapq.heappush(q,(0,0,0))

    while q:
        cost,x,y = heapq.heappop(q)

        if dist[x][y] < cost:
            continue
        for d in range(4): # 4방향 이동하면서 인접노드 확인
            nx,ny = x+dx[d], y+dy[d]
            if nx<0 or nx>=m or ny<0 or ny >=n:
                continue
            new_cost = cost + board[nx][ny]
            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(q,(new_cost,nx,ny))

dijkstra()
print(dist[m-1][n-1])
