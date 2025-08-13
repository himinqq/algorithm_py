import heapq
from heapq import heapify


def solution(n, works):
    answer = 0
    # 야근피로도 =(야근시작시점에서 남은 일의 작엽량)^2
    # work 에서 최대 n 만큼 빼서 제곱 수 최소되는 값
    if n > sum(works):
        return 0
    over_works = [-w for w in works]
    heapify(over_works)
    for _ in range(n):
        w = heapq.heappop(over_works)
        w += 1
        heapq.heappush(over_works,w)

    return sum(w ** 2 for w in over_works)
