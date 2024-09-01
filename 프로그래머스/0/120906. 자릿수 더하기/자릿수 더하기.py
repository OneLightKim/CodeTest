def solution(n):
    answer = 0
    n = str(n)
    print(n)
    for i in n:
        answer += int(i)
    return answer