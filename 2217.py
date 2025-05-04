# 로프 이용하여 들어올릴 수 있는 물체의 최대 중량
# n개의 로프 사용 w인 물체 들어올리면 각 로프에는 w/n 만큼의 중량
# 모든 로프를 사용할 필요는 없음

#20인 물체 2개로프
#각 로프에는 20/2=10 만큼의 중량

#5 100 300
#큰 로프 순으로 정렬 300 100 5
#로프 100선택 > 최솟값*n(로프수)을 넘으면 안됨 => 100*2 최대 200
#로프 5선택 => 최대 15
#최대 중량은 300

#그리디 전략
#로프 내림차순 정렬, 가장 약한 로프 기준으로 전체 하중 

#로프 개수
n = int(input())
#각 로프가 버틸 수 있는 최대 중량
weights = [int(input()) for _ in range(n)]
weights.sort(reverse=True)

currMax = weights[0]
for i in range(1,n):
    mx = weights[i]*(i+1) #가장 약한로프*로프 수
    currMax = max(currMax,mx)
print(currMax)

