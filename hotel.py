import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    answer = []
    hotel = {}

    def find(n):
        if n not in hotel:
            hotel[n] = n+1
            return n
        hotel[n] = find(hotel[n])
        return hotel[n]
    for num in room_number:
        answer.append(find(num))

    return answer
