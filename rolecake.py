from collections import Counter

def solution(topping):
    answer = 0
    cheolsu = set()
    broth = Counter(topping)

    for top in topping:
        cheolsu.add(top)
        broth[top] -= 1
        if broth[top] == 0:
            del broth[top]
        if len(broth) == len(cheolsu):
            answer+= 1
    return answer