def solution(s):
    a, b = 0, 0
    for i in s:
        if i == '(':
            a += 1
        elif i == ')' and a == 0:
            return False
        elif i == ')' and a != 0:
            b += 1
        if b > a:
            return False
    if a == b:
        return True
    else:
        return False