def solution(a, b):
    answer = 0
    list_ab = [a,b]
    min_ab = min(list_ab)
    max_ab = max(list_ab)
    for i in range(min_ab,max_ab+1):
        answer += i
    return answer