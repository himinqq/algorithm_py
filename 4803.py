# 그래프 주어졌을 때 트리 개수 세기
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# 사이클 여부 확인
def dfs(cur, par):
    vis[cur] = True
    for adj in graph[cur]:
        if adj == par:  # (무방향) 부모 -> 자식 방향으로만 탐색. 부모 간선 무시
            continue
        if vis[adj]:  # 부모가 아닌데 방문되었다 -> 사이클!
            return False
        if not dfs(adj, cur):  # 새로운 노드 탐색 및 결과 전파
            return False  # 자식에서 사이클 발견(False)되면 부모에게 알림. (탐색 종료)
    return True


N, M = map(int, input().split())
case = 1
while (N, M) != (0, 0):
    graph = [[] for _ in range(N + 1)]
    vis = [False] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    for node in range(1, N + 1):
        if not vis[node]:
            if dfs(node, -1):
                cnt += 1
    if cnt == 0:
        msg = "No trees."
    elif cnt == 1:
        msg = "There is one tree."
    else:
        msg = f"A forest of {cnt} trees."

    print(f"Case {case}: {msg}")
    case += 1
    N, M = map(int, input().split())
