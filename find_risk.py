from collections import Counter


def solution(points, routes):
    answer = 0
    spots = [i for i in points]

    def move(route):
        idx = 0
        path = []
        for i in range(len(route) - 1):
            sx,sy = spots[route[i] - 1]
            ex,ey = spots[route[i + 1] - 1]
            # ㅌ좌표를 한 칸씩 움직이며 경로를 기록
            while sx != ex:
                path.append((sx, sy, idx))
                # sx가 ex보다 작으면 sx를 1씩 증가시키고(오른쪽으로 이동), 크면 1씩 감소시킵니다(왼쪽으로 이동).
                if sx < ex:
                    sx += 1
                else:
                    sx -= 1
                idx += 1 # 이동할 때마다 idx(시간)를 1씩 증가시켜, 움직인 시간 정보를 기록
            # y좌표를 한 칸씩 움직이며 경로를 기록
            while sy != ey:
                path.append((sx, sy, idx))
                if sy < ey:
                    sy += 1
                else:
                    sy -= 1
                idx += 1
        path.append((sx, sy, idx))
        return path
    second = []
    for route in routes:
        second.extend(move(route))
    counted = Counter(second)
    for i in counted.values():
        if i >= 2:
            answer += 1
    return answer