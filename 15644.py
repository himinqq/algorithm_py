from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            red_ball = (i, j)
        elif board[i][j] == 'B':
            blue_ball = (i, j)


def move(x, y, d):
    cnt = 0
    while True:
        if board[x][y] == 'O' or board[x + dx[d]][y + dy[d]] == '#':
            break
        x += dx[d]
        y += dy[d]
        cnt += 1
    return x, y, cnt


vis = set()
dx = [-1, 0, 1, 0] #북U동R남D서L
dy = [0, 1, 0, -1]
dir = ['U','R','D','L']

def bfs():
    q = deque()
    rx, ry = red_ball
    bx, by = blue_ball
    q.append((rx, ry, bx, by, 0,[]))
    vis.add((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, depth, path = q.popleft()
        if depth >= 10:
            break
        for d in range(4):
            nrx, nry, rc = move(rx, ry, d)
            nbx, nby, bc = move(bx, by, d)

            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return depth+1,path + [dir[d]]

            if nrx==nbx and nry==nby:
                if rc > bc:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]
            if (nrx,nry,nbx,nby) not in vis:
                q.append((nrx,nry,nbx,nby,depth+1,path + [dir[d]]))
                vis.add((nrx,nry,nbx,nby))
    return -1,[]

res, ans_dir = bfs()
print(res)
print(''.join(ans_dir))
