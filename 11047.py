n, k = map(int, input().split())

lst = [int(input()) for i in range(n)]

lst.sort(reverse=True)

ans = 0

for value in lst:
    if k >= value:
        ans += k // value
        k %= value
print(ans)