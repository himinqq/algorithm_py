# 풀이설명1 : 함수 만들기
def solution(book_time):
    def change_min(str_time: str) -> int:
        return int(str_time[0:2]) * 60 + int(str_time[3:])

    book_times = sorted([[change_min(i[0]), change_min(i[1]) + 10] for i in book_time])
    rooms = []
    for book_time in book_times:
        if not rooms:
            rooms.append(book_time)
            continue
        for index, room in enumerate(rooms):
            if book_time[0] >= room[-1]: #index 방 마지막예약 끝나는 시간보다 크거나 같으면 배정 가능
                rooms[index] = room + book_time #기존 방에 추가하기
                break
        else:
            rooms.append(book_time) #기존의 방에 배정할 수 없으면, 새로운 방에 배정
    return len(rooms)
