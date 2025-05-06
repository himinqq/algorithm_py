from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]

vis = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

    q = deque([(x,y)])
    vis[x][y] = True
    area = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if graph[nx][ny] == 0 or vis[nx][ny]:
                continue
            vis[nx][ny] = True
            q.append((nx,ny))
            area += 1
    return area

cnt = 0
mx = 0
for i in range(n):
    for j in range(m):
        #그림0 이고, 방문했으면 건너뛰기
        if graph[i][j] == 0 or vis[i][j]:
            continue
        #bfs 실행할 때마다 개수 세기
        cnt += 1
        sz = bfs(i,j)
        mx = max(mx,sz)

print(cnt)
print(mx)