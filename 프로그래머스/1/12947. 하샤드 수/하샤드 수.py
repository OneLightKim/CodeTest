def solution(n):
    answer = 0
    arr_n = list(str(n))
    for i in arr_n:
        answer += int(i)
    if n%answer == 0:
        return True
    else:
        return False
