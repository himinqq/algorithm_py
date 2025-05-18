
used = [False] * 50
arr = [0] * 6
def backtrack(k,n,start):
    if k == 6:
        print(*arr)
        return
    for i in range(start,n+1):
        if not used[i]:
            arr[k] = numbers[i]
            used[i] = True
            backtrack(k+1,n,i)
            used[i] = False

numbers = list(map(int,input().split()))
while numbers[0] != 0:
    k = numbers[0]
    backtrack(0,k,1)
    print()
    numbers = list(map(int, input().split()))