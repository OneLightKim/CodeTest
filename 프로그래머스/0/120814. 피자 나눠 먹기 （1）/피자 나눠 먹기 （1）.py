def solution(n):
    if n>7:
        answer = n//7+1 if n/7>n//7 else n//7
    else:
        answer = 1
    return answer