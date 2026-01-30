def solution(n):
    answer = 0
    a = str(bin(n)[2:])
    while True:
        n += 1
        b = str(bin(n)[2:])
        if b.count('1') == a.count('1'):
            break
    return n