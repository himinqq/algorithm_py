import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([(x,y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: #방문하지 않은 칸만 큐에 넣기
                graph[nx][ny] = graph[x][y]+ 1 #현재칸(x,y)의 거리 +1
                q.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))

