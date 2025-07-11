n = int(input())

arr = list(map(int, input().split()))
dp = [0] * n

for curr in range(n):
    dp[curr] = 1
    for search in range(curr):
        if arr[curr] > arr[search]:
            dp[curr] = max(dp[curr], dp[search] + 1)

print(max(dp))
