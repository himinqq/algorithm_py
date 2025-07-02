import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int,input().split()))

left, right = 0,0
tot = 0
ans = float('inf')

while right < n:
    # right 오른쪽으로 옮겨가며 더함
    tot += arr[right]
    right += 1

    while tot >= s: #조건 만족
        ans = min(ans, right - left) #정답 갱신
        tot -= arr[left]
        left += 1

print(ans if ans!= float('inf')else 0)