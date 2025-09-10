INF = float('inf')
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# N개 도시 모두 방문한 상태
END = (1 << N) - 1 # 모든 도시 방문했는지 확인하기 위한 비트마스크  (N개의 비트를 전부 1로 세팅한 값)

# 현재도시 now에 있고, vis 상태일 때 남은 도시를 방문하고 돌아오는 최소 비용 저장
dp = [[None] * (1 << N) for _ in range(N)]


def tsp(now, vis):
    if vis == END: # 모든 도시 방문한 상태면
        # 시작도시(0번)으로 돌아가는 비용 반환, 돌아가는 길 없으면 INF 반환
        return cost[now][0] if cost[now][0] else INF

    if dp[now][vis] is not None: # 계산 값 있으면, 그 값 반환
        return dp[now][vis]

    best = INF # 최소 비용 찾기
    for nxt in range(N): # 현재 도시에서 방문하지 않은 도시 중 하나를 선택해 재귀적으로 탐색

        # now->nxt로 가는 길이 없거나, nxt 도시 이미 방문했다면 스킵
        if cost[now][nxt] == 0 or vis & (1 << nxt):
            continue

        # nxt 도시를 방문하는 경로 비용 계산
        temp = tsp(nxt, vis | (1 << nxt)) # nxt 방문을 표시 (vis에 nxt 비트를 켜기)
        best = min(best, cost[now][nxt] + temp)  # 현재까지의 최소 비용 갱신
    dp[now][vis] = best # 최소 비용 저장
    return best

# 0번 도시에서 시작, 0번 도시만 방문한 상태(vis=1)로 시작
print(tsp(0,1))

