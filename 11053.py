
n = int(input())
numbers = list(map(int,input().split()))

# dp[i[ = i번째 수에서 길이 최대
dp = [1]*n
for i in range(1,n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))

