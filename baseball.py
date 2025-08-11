# 1번 선수는 4번 타자로 결정됨
# 타순 정하기
# 각 이닝의 결과 미리 알고 있음. 최다 득점 하는 타순 찾고 그 때의 득점 수 리턴
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
infos = [list(map(int,input().split())) for _ in range(N)]

# 점수 계산: 루에 있는 주자들의 이동에 따라 득점이 계산되어야 함
# b1,b2,b3(1·2·3루 상태)를 관리하고, 히트 종류에 따라 주자 이동/득점 업데이트
def play(infos, order):
    score = 0
    batter = 0
    n = len(infos)

    for inning in range(n):
        out_count = 0
        b1 = b2 = b3 = 0
        while out_count < 3:
            res = infos[inning][order[batter]]
            if res == 0:
                out_count += 1

            elif res == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif res == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif res == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif res == 4:
                score += b1 + b2 + b3 + 1
                b1 = b2 = b3 = 0
            batter = (batter + 1) % 9
    return score

max_score = 0
for p in permutations(range(1,9),8):
    order = list(p[:3]) + [0] + list(p[3:]) #   # 1번 선수는 4번 타자(인덱스 3)로 고정
    max_score = max(max_score, play(infos, order))
print(max_score)