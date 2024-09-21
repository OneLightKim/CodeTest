def solution(spell, dic):
    for i in dic:
        count = 0
        for j in spell:
            if j in i:
                count += 1
        if count == len(spell):
            answer = 1
            break
        else:
            answer = 2
    return answer