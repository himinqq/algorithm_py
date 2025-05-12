n, m = map(int,input().split())

numbers = list(map(int, input().split()))

numbers.sort()

arr = [0]* m
used = [False] * n

def backtrack(k):
    if k == m:
        print(*arr)
        return
    for i in range(n):
        if not used[i]:
            arr[k] = numbers[i]
            used[i] = True

            backtrack(k+1)
            used[i] = False
backtrack(0)


