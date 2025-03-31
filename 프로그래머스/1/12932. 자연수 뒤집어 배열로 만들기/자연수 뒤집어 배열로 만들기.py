def solution(n):
    answer = []
    reversed_n = str(n)[::-1]
    answer = list(map(int,reversed_n))
    return answer