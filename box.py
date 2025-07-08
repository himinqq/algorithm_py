def solution(order):

    main = 1  # 현재 메인 컨테이너 벨트에서 꺼낼 상자 번호
    stack = []
    idx = 0  # order에서 현재 실어야 할 상자 위치

    while main <= len(order):
        if order[idx] == main:
            idx += 1
            main += 1
        elif stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
        else:
            stack.append(main)
            main += 1

    # 남은 stack 처리
    while stack and idx < len(order) and stack[-1] == order[idx]:
        stack.pop()
        idx += 1

    return idx
