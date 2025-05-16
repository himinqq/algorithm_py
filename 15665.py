
n,m = map(int,input().split())
numbers = list(map(int,input().split()))
arr = [0]*m
numbers.sort()
seen = set()

def backtrack(k):
    if k == m:
        key = tuple(arr)
        if key not in seen:
            print(*arr)
            seen.add(key)
        return
    for i in range(n):
        arr[k] = numbers[i]
        backtrack(k + 1)
backtrack(0)