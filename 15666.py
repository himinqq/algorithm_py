n,m = map(int,input().split())

arr = [0]*m
numbers = list(map(int,input().split()))
numbers.sort()

seen = set()

def backtrack(start,k):
    if k == m:
        key = tuple(arr)
        if key not in seen:
            seen.add(key)
            print(*arr)
        return
    for i in range(start,n):
        arr[k] = numbers[i]
        backtrack(i, k + 1)

backtrack(0,0)