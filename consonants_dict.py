from itertools import product


def solution(word): # 완전탐색
    words = ['A','E','I','O','U']
    my_dict = []
    for i in range(1,6):
        for prod in product(words, repeat=i):
            my_dict.append(''.join(prod))
    my_dict.sort()
    return my_dict.index(word) + 1

def solution2(word): #DFS
    words = "AEIOU"
    my_dict = []
    def dfs(depth,w):
        if depth == 5:
            return
        for i in range(len(words)):
            my_dict.append(w+words[i])
            dfs(depth+1,w+words[i])
    dfs(0,"")
    return my_dict.index(word) + 1