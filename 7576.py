# 익은 토마토의 상하좌우에 있는 익지 않은 토마토는 영향 받아 익음

# 모든 토마토가 익는 최소 일수 출력
# 단, 처음부터 모두 익어있으면 0, 익지 못하는 상황이면 -1 출력

# -1은 토마토 없음, 1익은토마토, 0익지않은 토마토

import sys
from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[0] * n for _ in range(m)]

ans = 0
q = deque()
# 시작점 여러개
# 모든 시작점 큐에 넣기
for i in range(m):
    for j in range(n):
        # 익은 토마토 큐에 넣기
        if graph[i][j] == 1:
            q.append((i, j))
        # 익지 않은 토마토 dist = -1
        if graph[i][j] == 0:
            dist[i][j] = -1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        #dist == 0 토마토 없거나 dist>0 이미 방문
        if dist[nx][ny] >= 0: continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))

for i in range(m):
    for j in range(n):
        if dist[i][j] == -1:
            print(-1)
            sys.exit(0)
        ans = max(ans,dist[i][j])
print(ans)
