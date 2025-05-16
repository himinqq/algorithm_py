n, m = map(int,input().split())
numbers = list(map(int,input().split()))

arr = [0]*m
used = [False]*n
numbers.sort()

seen = set()
def backtrack(start,k):
    if k == m:
        key = tuple(arr)
        if key not in seen:
            print(*arr)
            seen.add(key)
        return
    for i in range(start,n):
        if not used[i]:
            arr[k] = numbers[i]
            used[i] = True
            backtrack(i,k+1)
            used[i] = False

backtrack(0,0)