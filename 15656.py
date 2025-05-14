
n,m = map(int,input().split())
numbers = list(map(int,input().split()))

numbers.sort()
arr = [0] * m

def backtrack(k):
    if k == m:
        print(*arr)
        return
    for i in range(n):
       arr[k] = numbers[i]
       backtrack(k+1)

backtrack(0)



