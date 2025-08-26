def solution(tickets):
    tickets.sort() # 사전순 정렬
    n = len(tickets)
    answer = []
    vis = [False] * n # 티켓 기준으로 방문 처리

    def dfs(idx, path):
        if idx == n:
            answer.append(path[:])
            return
        for i in range(n):
            if not vis[i] and path[-1] == tickets[i][0]:
                vis[i] = True
                dfs(idx + 1, path + [tickets[i][1]])
                vis[i] = False

    dfs(0, ["ICN"])

    return min(answer) # 사전순으로 앞선 경로
