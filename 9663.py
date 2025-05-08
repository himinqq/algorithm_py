
#queen 은 상하좌우와 대각선으로 공격

import sys
input = sys.stdin.readline

n = int(input().strip())

# 열 사용 여부
isused_col = [False] * n
# '/' 대각선 사용 여부
isused_d1 = [False] * (2 * n)
# '\' 대각선 사용 여부
isused_d2 = [False] * (2 * n)

count = 0

def place_queen(row):
    global count
    if row == n:
        count += 1
        return
    for col in range(n):
        if isused_col[col]:
            continue
        if isused_d1[row + col]:
            continue
        if isused_d2[row - col + n - 1]:
            continue

        # 퀸 놓기
        isused_col[col] = True
        isused_d1[row + col] = True

        # x+y와 x-y는 -(n-1) ~ (n-1) 사이의 값을 가짐
        # (n-1) 더해서 0 ~ 2(n-1) 로 인덱스가 양수범위 가지도록 만든다
        # 원래 4면 -3부터 3까지 범위 가짐
        # 인덱스 양수로 만들기 위해 3더해서(4-1) 0부터 6으로 만든 것
        isused_d2[row - col + n - 1] = True

        place_queen(row + 1)

        # 되돌리기
        isused_col[col] = False
        isused_d1[row + col] = False
        isused_d2[row - col + n - 1] = False

place_queen(0)
print(count)
