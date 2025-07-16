
def dfs(v, graph, vis):
    vis[v] = True
    cnt = 1
    for adj in graph[v]:
        if not vis[adj]:
            cnt += dfs(adj, graph, vis)
    return cnt

def solution(n, wires):
    answer = -1

    # 간선 하나씩 제거해보기
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        vis = [False] * (n+1)

        # i번째 간선을 빼고 그래프 구성
        for j, (x, y) in enumerate(wires):
            if i == j:
                continue
            graph[x].append(y)
            graph[y].append(x)

        tmp = []
        for node in range(1, n+1):
            if not vis[node]:
                tmp.append(dfs(node, graph, vis))

        diff = abs(tmp[0] - tmp[1])
        if answer == -1 or diff < answer:
            answer = diff

    return answer
