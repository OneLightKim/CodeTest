from collections import Counter
def solution(topping):
    answer = 0
    dic = Counter(topping)
    set1 = set()
    for i in topping:
        dic[i] -= 1
        set1.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set1):
            answer += 1
    return answer