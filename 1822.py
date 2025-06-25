
an,bn = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

def binary_search(nums,target,start,end):
    if start > end:
        return False

    mid = (start+end) //2

    if nums[mid] == target:
        return True
    elif nums[mid] < target:
        return binary_search(nums,target,mid+1,end)
    else:
        return binary_search(nums,target,start,mid-1)

# a 에는 있고 b 에는 없는 원소
# b 에서 target=a 찾기 > 못찾으면 ans 에 append
ans = []
b.sort()
for tar in a:
    if binary_search(b,tar,0,bn-1) is False:
        ans.append(tar)
ans.sort()
print(len(ans))
print(*ans)