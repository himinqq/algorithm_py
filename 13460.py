from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 0, 1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]

# 빨간 구슬, 파란 구슬, 구멍 위치 초기화
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red_start = (i, j)
        elif board[i][j] == 'B':
            blue_start = (i, j)

def move(x, y, d):
    cnt = 0
    # 벽 만나거나 구멍 들어갈 때까지 이동
    while board[x + dx[d]][y + dy[d]] != '#' and board[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        cnt += 1
    return x, y, cnt

def bfs():
    q = deque()
    rx, ry = red_start
    bx, by = blue_start


    # 리스트는 visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    # visited[red_x][red_y][blue_x][blue_y] = True / False

    # 방문 상태를 set으로 관리: (rx, ry, bx, by)
    visited = set()
    visited.add((rx, ry, bx, by))
    q.append((rx, ry, bx, by, 0))

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth >= 10:
            break

        for d in range(4):  # 4방향 (네가지 동작이 가능하다)
            nrx, nry, rc = move(rx, ry, d)
            nbx, nby, bc = move(bx, by, d)

            # 파란 구슬이 구멍에 빠졌으면 실패
            # (파란 구슬이 구멍에 들어가면 안 된다.)
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠졌고 파란 구슬은 안 빠졌으면 성공
            if board[nrx][nry] == 'O':
                return depth + 1

            # 둘의 위치가 같으면, 이동 거리가 많은 쪽을 한 칸 뒤로
            # (빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. )
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))

    return -1

print(bfs())
