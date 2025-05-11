# 누적합 이용해서 구간 합 바르게 구하기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1) #누적합 저장할 배열 d[i] = a[1] + a[2] + ... + a[i]

# 누적합 배열 계산
# d[i] = d[i-1] + a[i] 를 이용하여 1부터 i까지의 합을 저장
for i in range(1, n + 1):
    d[i] = d[i - 1] + a[i]

# m개의 구간 합 질의 처리
for _ in range(m):
    i, j = map(int, input().split())
    # i부터 j까지의 합 = d[j] - d[i-1]
    # 전체 1~j 합에서 1~(i-1)까지의 합을 빼면 i~j 구간만 남음
    print(d[j] - d[i - 1])