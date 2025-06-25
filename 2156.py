n = int(input())
grapes = [int(input()) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

if n == 1:
    print(grapes[0])
    exit()
elif n == 2:
    print(grapes[0] + grapes[1])
    exit()

dp[0][1] = grapes[0]
dp[1][1] = grapes[1]
dp[1][2] = grapes[0] + grapes[1]

for i in range(2, n):
    dp[i][0] = max(dp[i - 1])  # 마시지 않은 경우
    dp[i][1] = max(dp[i - 2]) + grapes[i]  # i번째 포도주 1번 연속
    dp[i][2] = dp[i - 1][1] + grapes[i]  # i번째 포도주 2번 연속

print(max(dp[n - 1]))
