
N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

clouds = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]

for _ in range(M):
    d,s = map(int,input().split())
    for idx,(x,y) in enumerate(clouds):
        clouds[idx][0] = (x+dx[d-1]*s) % N
        clouds[idx][1] = (y+dy[d-1]*s) % N

    for x,y in clouds:
        board[x][y] += 1

    for x,y in clouds:
        cnt = 0
        for cross in range(1,8,2):
            nx,ny = x+dx[cross], y+dy[cross]
            if nx<0 or nx>=N or ny <0 or ny>= N:
                continue
            if board[nx][ny] > 0:
                cnt += 1
        board[x][y] += cnt

    new_clouds = []
    prev_clouds = set((x, y) for x, y in clouds)
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i,j) not in prev_clouds:
                new_clouds.append([i,j])
                board[i][j] -= 2

    clouds = new_clouds

ans = 0
for i in range(N):
    for j in range(N):
        if board[i][j] > 0:
            ans += board[i][j]

print(ans)






