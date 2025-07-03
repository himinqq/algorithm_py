n,m = map(int,input().split())
nums = list(map(int,input().split()))

# 수열의 부분 합이 m 이되는 경우의 수
start, end = 0,1
ans = 0
while end <= n:
    tot = sum(nums[start:end]) #시작점과 끝점을 정하기

    if tot <= m: #m보다 작거나 같으면 오른쪽 포인터 증가시킴
        if tot == m:
            ans += 1
        end += 1
    else: # m보다 크면 왼쪽 포인터 증가시킴
        start += 1

print(ans)