n = int(input())

graph = [list(map(int,input().strip())) for _ in range(n)]

ans = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

vis = [[False] * (n) for _ in range(n)]

def dfs(x,y,vis):
    vis[x][y] = True
    cnt = 1
    stack = [(x,y)]
    while stack:
        curr_x, curr_y = stack.pop()
        for i in range(4):
            nx, ny = curr_x+dx[i], curr_y+dy[i]
            if nx <0 or nx >=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1 and not vis[nx][ny]:
                stack.append((nx,ny))
                vis[nx][ny] = True
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not vis[i][j]:
            ans.append(dfs(i,j,vis))

ans.sort()
print(len(ans))
for a in ans:
    print(a)

