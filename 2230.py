n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

ans = float('inf')
start, end = 0, 0

while start <= end and end < n:
    if arr[end] - arr[start] < m:
        end += 1
    else:
        ans = min(ans, arr[end] - arr[start])
        start += 1

print(ans)
