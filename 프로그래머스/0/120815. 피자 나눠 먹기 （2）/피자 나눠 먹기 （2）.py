def solution(n):
    # while 1:
    #     i = 1
    #     if 6*i % n == 0:
    #         return i
    #         break
    #     else:
    #         i += 1
    for i in range(1,n+1):
        if 6*i%n == 0:
            return i
            break
            