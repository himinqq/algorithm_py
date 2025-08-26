N, K = map(int, input().split())
nums = list(map(int, input().split()))

# 최대 k 번 건너 뛸 수 있음
# 짝수로 이루어진 연속 부분 수열 가장 긴 길이

st, ed = 0, 0
skip = 0
ans = 0
while ed < N:
    if nums[ed] % 2 != 0: # 홀수면 건너 뛰기
        skip += 1

    while skip > K: # 홀수 k개 넘으면 st 이동 시키기
        if nums[st] % 2 != 0:
            skip -= 1
        st += 1

    ans = max(ans, ed - st + 1 - skip) # 현재 구간에서 짝수만 남긴 길이
    ed += 1

print(ans)
