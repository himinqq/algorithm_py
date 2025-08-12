def solution(triangle):
    n,m = len(triangle), len(triangle[0])
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if j == 0:
                dp[i][j] = dp[i-1][j]
            elif j == 1:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])

    return max(dp[n-1])