
n,m = map(int,input().split())

arr = [0] * m
used = [False] * n

numbers = list(map(int,input().split()))
numbers.sort()

def backtrack(k,start):
    if k == m:
        print(*arr)
        return
    for i in range(start,n): #i는 0123
        if not used[i]:
            arr[k] = numbers[i]
            used[i] = True
            backtrack(k+1,i+1)
            used[i] = False

backtrack(0,0)