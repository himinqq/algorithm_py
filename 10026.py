from collections import deque

n = int(input())
graph = [input() for _ in range(n)]
vis = [[False]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(color:str):
    ans = 0
    for i in range(n):
        for j in range(n):
            q = deque()
            if graph[i][j] == color and not vis[i][j]:
                q.append((i,j))
                vis[i][j] = True
                ans += 1
                while q:
                    currX,currY = q.popleft()
                    for k in range(4):
                        nx = currX + dx[k]
                        ny = currY + dy[k]
                        if nx <0 or nx>=n or ny<0 or ny>=n:
                            continue
                        if not vis[nx][ny] and graph[nx][ny] == color:
                            q.append((nx,ny))
                            vis[nx][ny] = True
    return ans


diff = bfs("R")+bfs("G")+bfs("B")

#적록색약 R G 동일하게 본다 => R이면 G로 만들고 G,B에 대해 BFS 돌리기
for i in range(n):
    graph[i] = graph[i].replace('R', 'G')

vis = [[False]*n for _ in range(n)]
same = bfs("G")+bfs("B")

#적록색약 아닌사람 구역개수, 적록색약이볼 때 구역 수 공백으로 구분 출력
print(diff,same)