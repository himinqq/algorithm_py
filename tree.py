import sys
sys.setrecursionlimit(10**6)
N = int(input())
input = sys.stdin.readline
parents = [-1] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def find_parents(cur,p):
    parents[cur] = p
    for adj in graph[cur]:
        if adj != p:
            find_parents(adj,cur)

find_parents(1,0)
for i in range(2,N+1):
    print(parents[i])

