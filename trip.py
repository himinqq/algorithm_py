from collections import deque


def solution(maps):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    vis = [[False] * m for _ in range(n)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        vis[x][y] = True
        total = int(maps[x][y])
        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if vis[nx][ny] or maps[nx][ny] == 'X':
                    continue
                q.append((nx, ny))
                vis[nx][ny] = True
                total += int(maps[nx][ny])
        return total

    for i in range(n):
        for j in range(m):
            if not vis[i][j] and maps[i][j] != 'X':
                answer.append(bfs(i, j))
    if not answer:
        return [-1]
    answer.sort()
    return answer
