n = int(input())
numbers = list(map(int, input().split()))

#dp[i] = i번째 수(numbers[i])를 마지막 원소로 하는 증가 부분 수열의 최대 합
dp = [0] * n
dp[0] = numbers[0]

for i in range(1, n):
    dp[i] = numbers[i]  # 일단 자기 자신만 포함했을 때로 시작
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + numbers[i])
print(max(dp))
