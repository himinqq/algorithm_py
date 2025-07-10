def solution(record):
    answer = []
    user = dict()

    r = []
    for str in record:
        r.append(str.split())
    
    for cmd,uid,name in r:
        user[uid] = name

    for cmd,uid,name in r:
        if cmd == "Enter":
            answer.append("{}님이 들어왔습니다.".format(user[uid]))
        elif cmd == "Leave":
            answer.append("{}님이 나갔습니다.".format(user[uid]))

    return answer