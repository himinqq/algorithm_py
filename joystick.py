def solution(name):
    answer = 0
    n = len(name)

    # 1. 각 문자 바꾸는 비용
    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)

    # 2. 좌우 이동 최소값 계산
    move = n - 1  # 아무리 최악이어도 문자열을 한번 순회하는 것

    for i in range(len(name)):
        idx = i + 1
        while idx < n and name[idx] == 'A':
            idx += 1
        move = min(move, (2*i) + len(name)-idx, 2* (len(name)-idx)+ i)

    answer += move
    return answer
