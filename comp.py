# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기
# 색인번호 출력 후 입력에서 w 제거
# 입력에서 남은 다음 글자 c 있으면 w+c를 사전에 등록

def solution(msg):
    answer = []
    # 초기 사전 생성
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k: v for (k, v) in zip(alphabet, list(range(1, 27)))}
    nxt_idx = 27

    i = 0
    # 현재 위치부터 가장 긴 w 찾기
    while i < len(msg):
        w = msg[i]
        j = i + 1

        # 슬라이딩 윈도우 (msg[i:j]식으로 탐색 범위 확장)
        while j <= len(msg) and msg[i:j] in d:
            w = msg[i:j]
            j += 1

        # 사전에서 w의 색인번호 출력
        answer.append(d[w])

        # w 다음글자 c 있으면, w+c를 사전에 추가
        if j <= len(msg):
            c = msg[j - 1]
            d[w + c] = nxt_idx
            nxt_idx += 1

        # w_idx는 길이만큼 이동
        i += len(w)

    return answer
