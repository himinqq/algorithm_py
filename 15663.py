from enum import unique

n,m = map(int,input().split())

numbers = [0] + list(map(int,input().split()))

numbers.sort()
arr = [0] * m
used = [False] * (n+1)

seen = set()

def backtrack(k):
    if k == m:
        key = tuple(arr)
        if key not in seen:
            print(*arr)
            seen.add(key)
        return
    for i in range(1,n+1):
        if not used[i]:
            arr[k] = numbers[i]
            used[i] = True
            backtrack(k+1)
            used[i] = False

backtrack(0)