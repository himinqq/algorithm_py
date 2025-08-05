from itertools import product


def solution(users, emoticons):
    DISCOUNT = [0.1, 0.2, 0.3, 0.4]
    rates = list(product(DISCOUNT, repeat=len(emoticons)))

    result = []
    for i in range(len(rates)):
        total_price = 0
        membership_cnt = 0
        for percent, max_price in users:
            rate = percent / 100
            purchase = 0
            for idx, emo_price in enumerate(emoticons):
                if rates[i][idx] >= rate:
                    purchase += emo_price - (emo_price * rates[i][idx])
            if purchase < max_price:
                total_price += purchase
            else:
                membership_cnt += 1
        result.append([membership_cnt, int(total_price)])

    return max(result, key=lambda x: (x[0], x[1]))

# 자신의 할인 기준 이상이면  이모티콘 모두 구매
# 설정 금액보다 구매 금액 높으면 취소하고 플러스 서비스 가입
# 플러스서비스 가입자수와 이모티콘 매출액 리턴
# 가입자 수 최대가 첫번째 목표
# 할인율은 10%, 20%, 30%, 40% 중 하나로 설정. 이모티콘마다 할이율 다를 수 있음
