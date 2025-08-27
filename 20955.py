import sys
input = sys.stdin.readline

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b: # 이미 같은 집합이면 사이클
        return False
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return True

N, M = map(int,input().split())
parent = [0]* (N+1)
for i in range(1,N+1):
    parent[i] = i

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

ans = 0
# 사이클 만드는 간선 확인
for _ in range(M):
    u,v = map(int,input().split())
    if not union(u,v):
        ans += 1

 # i와 i+1 연결되어있지 않으면 연결
for i in range(1,N):
    if find(i) != find(i+1):
        union(i,i+1)
        ans += 1

print(ans)
