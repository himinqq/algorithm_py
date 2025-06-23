n = int(input())
nums = list(map(int,input().split()))

m = int(input())
targets = list(map(int,input().split()))
nums.sort()

def binary_search(arr,target,start,end):
    if start > end:
        return False
    mid = (start+end) //2

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,end)
    else:
        return binary_search(arr,target,start,mid-1)

for tar in targets:
    if binary_search(nums,tar,0,len(nums)-1):
        print(1)
    else:
        print(0)


