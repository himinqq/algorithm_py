#현재 회의가 끝나는 시점 이후에 시작하는 회의 중 가장 먼저 끝나는 것

n = int(input())
times = [list(map(int, input().split())) for i in range(n)]

# 종료 시간 기준 정렬
times.sort(key=lambda x:(x[1],x[0]))

cnt = 1
curT = times[0][1]

for i in range(1, len(times)):
    nxtS = times[i][0]
    if curT <= nxtS:
        cnt += 1
        curT = times[i][1]

print(cnt)



