# 돈 인출하는데 필요한 합의 최솟값 출력

#사람 수
n = int(input())

times = list(map(int,input().split()))

times.sort()

waitT = 0
for i in range(0,n):
    for j in range(0,i+1):
        waitT += times[j]

print(waitT)