import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int,input().split())
boss_of = list(map(int, input().split()))
compliments = [0] * (N+1)

# 각 직원이 상사일 때 부하 직원들 리스트
child = [[] for _ in range(N+1)]

# 상사의 자식 목록에 i 번 직원 추가
for i in range(2,N+1):
    child[boss_of[i - 1]].append(i)

def dfs(cur):
    for nxt in child[cur]:
        compliments[nxt] += compliments[cur]
        dfs(nxt)

for _ in range(M):
    i, w = map(int,input().split())
    compliments[i] += w

dfs(1)

for i in range(1,N+1):
    print(compliments[i],end=" ")