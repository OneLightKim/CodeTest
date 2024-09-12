def solution(i, j, k):
    answer = 0
    for a in range(i, j+1):
        c = str(a)
        c = list(c)
        for l in c:
            if str(k) in l:
                answer += 1
    return answer