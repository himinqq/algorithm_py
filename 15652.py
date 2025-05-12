
n, m = map(int,input().split())
# 1,2 와 2,1 은 중복으로
arr = []

def func(k,start):
    if k == m:
        print(*arr)
        return
    for i in range(start,n+1):
        arr.append(i)
        func(k+1,i)
        arr.pop()

func(0,1)
