from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    applicants = defaultdict(list)

    # 지원자 정보 입력
    for i in info:
        i = i.split()
        for lan in [i[0], '-']:
            for job in [i[1], '-']:
                for career in [i[2], '-']:
                    for food in [i[3], '-']:
                        applicants[lan+job+career+food].append(int(i[4]))

    # 점수 리스트 정렬
    for key in applicants:
        applicants[key].sort()

    # 쿼리 처리
    for q in query:
        q = q.replace("and ", "").split()
        score = int(q[-1])
        key = "".join(q[:-1])

        scores = applicants[key]
        idx = bisect.bisect_left(scores, score)  # score 이상 시작 인덱스
        answer.append(len(scores) - idx)

    return answer
