from collections import Counter


def solution(weights):
    answer = 0

    # 1:1
    counter = Counter(weights)
    for key, value in counter.items():
        if value >= 2:
            answer += value * (value - 1) // 2

    weights = set(weights)  # 1:1 구한 후 중복 제거

    # 2:3, 2:4, 3:4
    for w in weights: # w와 시소 짝꿍이 되기 위해 필요한 무게가 weights 안에 있는가?
        if w * 2 / 3 in weights: # 현재 무게 w가 “3칸 쪽에 앉았을 때” → 2칸 쪽에 앉아서 시소를 평형 맞출 수 있는 상대의 무게를 계산
            answer += counter[w * 2 / 3] * counter[w]
        if w * 2 / 4 in weights:
            answer += counter[w * 2 / 4] * counter[w]
        if w * 3 / 4 in weights:
            answer += counter[w * 3 / 4] * counter[w]
    return answer