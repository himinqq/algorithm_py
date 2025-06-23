# n 보다 작은 수의 개수
n = int(input())

nums = list(map(int,input().split()))

from bisect import bisect_left
uniq = sorted(set(nums))

for num in nums:
    print(bisect_left(uniq,num), end=" ")