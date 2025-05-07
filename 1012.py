from collections import deque

t = int(input())

# 가로, 세로, 배추 심어진 위치 개수
# 이후 k번 (x,y)배추 위치

# 필요한 최소의 배추흰지렁이 마리 수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    n, m, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 or vis[i][j]:
                continue

            q = deque()
            q.append((i, j))
            vis[i][j] = True

            cnt += 1

            while q:
                currX, currY = q.popleft()
                for v in range(4):
                    nx = currX + dx[v]
                    ny = currY + dy[v]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if vis[nx][ny] or graph[nx][ny] == 0:
                        continue
                    q.append((nx, ny))
                    vis[nx][ny] = True
    print(cnt)
