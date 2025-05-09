# from itertools import combinations
# nums = [i for i in range(1,n+1)]
# nums.sort()
# for i in combinations(nums,m):
#     print(*i)

n, m = map(int, input().split())
# 길이 m인 조합 만들기
arr = [0]*m
used = [False]* (n+1)
seen = set() #중복 검사

def func(k):
    if k == m:
        key = tuple(sorted(arr))
        if key not in seen:
            seen.add(key)
            print(*arr)
        return
    for i in range(1,n+1):
        if not used[i]:
            arr[k] = i
            used[i] = True
            func(k+1)
            used[i]= False

func(0)


