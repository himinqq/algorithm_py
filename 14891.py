# n극 0 s극 1
# 톱니바퀴 4개
from collections import deque

RIGHT = 2
LEFT = 6
wheels = [0] + [deque(map(int, input().strip())) for _ in range(4)]

# [1] 회전 방향 미리 기록
def get_rotate(start, direction):
    rot = [0] * 5 # 인덱스 1번부터, 톱니바퀴의 회전 방향 담기
    rot[start] = direction
    # [2] 양옆으로 전파하면서 반대방향 결정
    for i in range(start, 4): #오른쪽 전파
        if wheels[i][RIGHT] != wheels[i + 1][LEFT]:
            rot[i + 1] = -rot[i] #다르면 반대 방향으로 회전
        else: #서로 같은 극이면 중지
            break
    for i in range(start, 1, -1): #왼쪽 전파
        if wheels[i][LEFT] != wheels[i - 1][RIGHT]:
            rot[i - 1] = -rot[i]
        else:
            break
    return rot

# [3] 최종 회전 실행
def apply_rotation(rot):
    for i in range(1, 5):
        if rot[i]:
            wheels[i].rotate(rot[i])
# 회전 횟수 k
k = int(input())
# 회전시킨 방법 (톱니바퀴 번호, 방향) 1시계 -1반시계
for _ in range(k):
    num, direc = map(int, input().split())
    rotations = get_rotate(num, direc)
    apply_rotation(rotations)

# [4] 점수 계산
tot = 0
score = 1
for i in range(1, len(wheels)):
    if wheels[i][0] == 1:
        tot += score
    score *= 2
print(tot)



