from collections import deque


def solution(land):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = len(land), len(land[0])

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        vis[x][y] = True
        cols = set()
        cols.add(y)
        cnt = 1

        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if vis[nx][ny] or land[nx][ny] != 1:
                    continue
                q.append((nx, ny))
                vis[nx][ny] = True
                cols.add(ny)
                cnt += 1

        return cnt, cols

    vis = [[False] * m for _ in range(n)]
    col_size = [0] * m

    for i in range(n):
        for j in range(m):
            if not vis[i][j] and land[i][j] == 1:
                size, cols = bfs(i, j)
                for col in cols:
                    col_size[col] += size
    return max(col_size)
