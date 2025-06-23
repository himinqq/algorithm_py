from bisect import bisect_left,bisect_right

def count_by_range(a,left,right):
    return bisect_right(a,right) - bisect_left(a,left)

n = int(input())
nums = list(map(int,input().split()))
nums.sort()

m = int(input())
targets = list(map(int,input().split()))

for tar in targets:
    print(count_by_range(nums,tar,tar),end=" ")