import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

ans = 0
arr.sort()

ans = 0
cnt = Counter(arr)

# arr[i] 고정하고 나머지 두 수 arr[st], arr[ed]를 투포인터 방식으로 찾아서 합이 0이 되는 경우 찾기
for i, a in enumerate(arr):
    st, ed = i + 1, N - 1
    while st < ed:
        s = arr[st] + arr[ed] + arr[i]
        if s == 0:
            if arr[st] == arr[ed]:  # 두 포인터 값 같으면 중복 수 처리
                ans += ed - st
            else:  # 오른쪽 값 여러번 나오면 그 개수만큼 더함
                ans += cnt[arr[ed]]
            st += 1
        elif s > 0:
            ed -= 1
        else:
            st += 1

print(ans)
