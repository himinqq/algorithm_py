from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        combi_list = []
        for order in orders: # 손님 한 명의 주문 마다 알파벳 순 정렬 후 길이 c인 모든 조합 생성
            combi_list += list(combinations(sorted(order),c))
            print(combi_list)
        count_dict = Counter(combi_list)
        for k,v in count_dict.items():
            if v >= 2 and v == max(count_dict.values()):
                answer.append("".join(k))

    return sorted(answer)