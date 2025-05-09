import sys
input = sys.stdin.readline
from collections import deque

m,n,h = map(int,input().split())

graph = []
for _ in range(h):
    tmp = [list(map(int, input().split())) for i in range(n)]
    graph.append(tmp)

# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토,
# 정수 -1은 토마토가 들어있지 않은 칸

#토마토 익는데 걸린 일수, 안익으면 -1
dis = []
for _ in range(h):
    tmp = [[0]*m for i in range(n)]
    dis.append(tmp)

dir = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

q = deque()

for i in range(n):
    for j in range(m):
        for k in range(h):
            #안익은 토마토는 -1로 초기화
            if graph[k][i][j] == 0:
                dis[k][i][j] = -1
            #익은 토마토 있으면 큐에 넣기
            if graph[k][i][j] == 1:
                q.append((i,j,k))

while q:
    x,y,z = q.popleft()
    for dx,dy,dz in dir:
        nx = x + dx
        ny = y + dy
        nz = z + dz
        # nz는 0과 h사이
        if nx <0 or nx>=n or ny<0 or ny>=m or nz<0 or nz >=h:
            continue
        #안익은 토마토 있는 곳에만 전파
        if dis[nz][nx][ny] == -1:
            dis[nz][nx][ny] = dis[z][x][y] + 1
            q.append((nx, ny, nz))

day = 0
for i in range(n):
    for j in range(m):
        for k in range(h):
            if dis[k][i][j] == -1:
                print(-1)
                sys.exit(0)
            day = max(day,dis[k][i][j])

print(day)