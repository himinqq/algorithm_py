N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]


# dp[mask][artist][price]:
# mask: 지금까지 그림 산 사람들의 집합 (비트마스크)
# artist: 현재 그림을 소유한 사람
# price: 최근 그림을 산 가격

# 현재 상태에서 앞으로 더 살 수 있는 최대 사람 수
dp = [[[0] * 10 for _ in range(N)] for _ in range(1 << N)]



def dfs(now, artist, cost):
    if dp[now][artist][cost] != 0:
        return dp[now][artist][cost]

    cnt = 0 # 앞으로 추가로 그림을 살 수 있는 최대 인원 수

    for i in range(1, N):  # 다음으로 그림을 살 후보자 i

        # 현재 cost보다 작거나, i번이 이미 그림을 산 적이 있으면 스킵
        if arr[artist][i] < cost or now & (1 << i):
            continue

        cnt = max(cnt, 1 + dfs(now | (1 << i), i, arr[artist][i]))
        # dfs 는 새로 사는 사람 수만 세므로, 맨 처음 소유자(0번) 포함하기 위해 + 1
        # now | (1<<i): i번을 산 사람 목록에 추가
        # i: 새로운 그림 소유자
        # arr[artist][i]: 새로운 거래 가격

    dp[now][artist][cost] = cnt
    return cnt


#
print(dfs(1, 0, 0) + 1)
