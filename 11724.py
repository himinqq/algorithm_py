# 무방향그래프 연결 요소 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

vis = [False] * (n+1)
def dfs(start):
    vis[start] = True

    for adj in graph[start]:
        if not vis[adj]:
            dfs(adj)
ans = 0
for i in range(1,n+1):
    if not vis[i]:
        dfs(i)
        ans += 1
print(ans)