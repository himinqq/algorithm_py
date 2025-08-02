from itertools import combinations


def solution(relation):
    # 컬럼 조합 구하기
    row = len(relation)
    col = len(relation[0])
    combi_keys = []
    for i in range(1, col + 1):
        combi_keys.extend(combinations(range(col), i))

    candi_keys = []
    for combi in combi_keys:
        # 유일성 확인 : 중복 제거한 튜플 개수가 릴레이션 행 개수와 같아야 함
        tmp = [tuple([item[i] for i in combi]) for item in relation]
        if len(set(tmp)) == row:
            # 최소성 확인
            if not any(set(ck).issubset(set(combi)) for ck in candi_keys):
                candi_keys.append(combi)

    return len(candi_keys)
