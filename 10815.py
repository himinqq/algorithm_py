import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
m = int(input())
targets = list(map(int,input().split()))

nums.sort()
def binary_search(num,target,start,end):
    if start > end:
        return False
    mid = (start + end) // 2

    if num[mid] == target:
        return True
    elif num[mid] < target:
        return binary_search(num,target,mid+1,end)
    else:
        return binary_search(num,target,start,mid-1)

ans = []
for tar in targets:
    if binary_search(nums,tar,0,len(nums)-1):
        ans.append(1)
    else:
        ans.append(0)
print(*ans)