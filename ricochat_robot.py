from collections import deque


def solution(board):
    n, m = len(board), len(board[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 시작(R)·목표(G) 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'G':
                gx, gy = i, j
            if board[i][j] == 'R':
                rx, ry = i, j

    # 현 위치(x,y)에서 dir_idx 방향으로 끝까지 미끄러진 뒤 좌표 반환
    def slide(x, y, d):
        while True:
            nx,ny = x+dx[d], y+dy[d]
            if nx < 0 or nx >= n or ny <0 or ny >= m or board[nx][ny] == 'D':
                return x,y
            x,y = nx,ny
    # bfs
    vis = [[False]*m for _ in range(n)]
    vis[rx][ry] = True
    q = deque()
    q.append((rx,ry,0))
    while q:
        x,y,cnt = q.popleft()
        if (x,y) == (gx,gy):
            return cnt
        for d in range(4):
            nx,ny = slide(x,y,d)
            if not vis[nx][ny]:
                vis[nx][ny] = True
                q.append((nx,ny,cnt+1))

    return -1
