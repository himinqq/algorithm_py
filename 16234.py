from collections import deque

N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q.append((x, y))
    union = []
    union.append((x, y))
    while q:
        curr_x, curr_y = q.popleft()
        for i in range(4):
            nx, ny = curr_x + dx[i], curr_y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if vis[nx][ny]:
                continue
            if L <= abs(world[curr_x][curr_y] - world[nx][ny]) <= R:
                q.append((nx, ny))
                union.append((nx, ny))
                vis[nx][ny] = True
    if len(union) <= 1:
        return 0
    result = sum(world[x][y] for x,y in union) // len(union)
    for x, y in union:
        world[x][y] = result
    return 1

day = 0
while True:
    stop = 0
    vis = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not vis[i][j]:
                vis[i][j] = True
                stop += bfs(i,j)
    if stop == 0:
        break
    day += 1

print(day)