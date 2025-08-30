T = int(input())

def find(p,x):
    if x != p[x]:
        p[x] = find(p,p[x])
    return p[x]

def union(p,a,b):
    a = find(p,a)
    b = find(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

for _ in range(T):
    N,M = map(int,input().split())
    edges = []
    parent = [i for i in range(N+1)]


    for _ in range(M):
        a,b = map(int,input().split())
        edges.append((a,b))

    ans = 0
    for edge in edges:
        a,b = edge
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            ans += 1

    print(ans)