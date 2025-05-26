n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
vis = [[False]*m for _ in range(n)]

vis[x][y] = True
cnt = 1

while True:
    flg = False
    for _ in range(4):
        d = (d+3) % 4 # 왼쪽으로 회전 (반시계90도)
        nx = x + dx[d]
        ny = y + dy[d]

        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if room[nx][ny] == 0 and not vis[nx][ny]:
            vis[nx][ny] = False
            cnt += 1
            x,y = nx,ny
            flg = True
            break
    if not flg:
        if room[x - dx[d]][y - dy[d]]:
            print(cnt)
            break
        else:
            x,y = x - dx[d], y - dy[d]