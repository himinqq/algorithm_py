from sys import stdin
input = stdin.readline

N = int(input())
dp = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(max(dp))