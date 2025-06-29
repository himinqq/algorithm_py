n = int(input())
m = int(input())
vip_seats = [int(input()) for _ in range(m)]

# 피보나치 배열 만들기 (자리 바꾸기 가능한 경우 수를 위한)
fib = [0] * (n + 2)
fib[0] = 1
fib[1] = 1
for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

# VIP 좌석 기준으로 구간 나눠서 경우의 수 곱하기
result = 1
prev_vip = 0  # 이전 VIP 좌석 (초기값은 0으로 시작)

for vip in vip_seats:
    gap = vip - prev_vip - 1  # VIP 사이의 일반 좌석 수
    result *= fib[gap]
    prev_vip = vip  # 다음 VIP 좌석 처리할 때 현재 VIP가 기준이 되도록 갱신

# 마지막 VIP 이후의 좌석도 처리
result *= fib[n - prev_vip]

print(result)
