#1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

n, m = map(int,input().split())

arr = [0] * m

def func(k):
    if k == m:
        print(*arr)
        return
    for i in range(1,n+1):
        arr[k] = i
        func(k+1)

func(0)