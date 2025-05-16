n = int(input())

schedule = [None] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 2)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1]) #이전 수익 유지

    t, p = schedule[i]
    end = i + t - 1
    if end <= n:  # 상담일이 퇴사일 안에 끝나야 함
        dp[end] = max(dp[end], dp[i - 1] + p) # i일에 상담할 경우 수익 반영

print(max(dp))
