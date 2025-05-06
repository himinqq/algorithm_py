
t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int,input().split()))

    #최대이익: 오늘 이후 최대가격 - 구매가격

    mx_future = 0
    gain = 0

    # 뒤에서부터 확인하면서, 미래의 최대가격 정보 저장
    # 즉, 미래의 최고점을 미리 기억해두고 오늘 가격보다 높으면 이익계산
    for price in reversed(prices):
        if price > mx_future:
            mx_future = price
        else:
            gain += mx_future - price

#[7, 3, 5, 1, 4]일 때
#앞에서부터 확인하면 3일때 (5,1,4)확인 후 최대값 5임을 알 수 있지만
#뒤에서부터 확인하면 3일때 최대값 5임을 미리 알 수 있다
