def solution(enroll, referral, seller, amount):
    # 자신의 이익 10%를 추천인에게 배분
    # 칫솔 하나에 100 원

    # enroll 은 노드
    # referral 은 각 노드의 부모 이름
    # seller , amount 는 각 노드가 판매한 칫솔 개수
    # 루트가 '-'인 트리에서 리프에서 루트까지 올라가기

    nodes = {e: idx for idx, e in enumerate(enroll)}
    N = len(enroll)
    parent = [-1] * N

    for i,p in enumerate(referral):
        parent[i] = nodes[p] if p != "-" else -1

    profit = [0] * N

    for s, a in zip(seller, amount):
        cur = nodes[s]
        money = a * 100
        while cur != -1 and money > 0:
            give = money // 10 # 10% 추천인에게 배분
            profit[cur] += (money - give) # 90% 자신이 갖기
            cur = parent[cur] # 다음 부모 노드 탐색
            money = give # 남은 돈 갱신

    return profit
