from itertools import combinations

def solution(number):
    answer = 0
    combinations_3 = list(combinations(number,3))
    n = len(combinations_3)
    for i in range(n):
        sam = combinations_3[i]
        if sum(sam) == 0:
            answer += 1
    return answer