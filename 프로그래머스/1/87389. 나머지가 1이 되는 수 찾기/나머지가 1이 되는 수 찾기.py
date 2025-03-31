def solution(n):
    answer = 0
    list_n = []
    for i in range(n):
        if n%(n-i) == 1:
            list_n.append(n-i)
        else:
            pass
    answer = min(list_n)
    return answer