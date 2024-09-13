from math import factorial
def solution(n):
    # answer=0
    # pac=1
    # a = 0
    # while True:
    #     stop=0
    #     pac=1
    #     a += 1
    #     for i in range(1,a+1):
    #         pac *= i
    #         if pac >= n:
    #             stop = 1
    #             break
    #     if stop==1:
    #         break
    # answer = a
    answer = 10
    while n < factorial(answer):
        answer -= 1
    return answer