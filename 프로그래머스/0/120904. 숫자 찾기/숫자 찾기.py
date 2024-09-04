def solution(num, k):
    # answer = 0
    # num = list(str(num))
    # for i in num:
    #     if i == k:
    #         answer = num.index(i)
    #         break
    # if answer == 0:
    #     return -1
    # else:
    #     return answer+1
    a = str(num).find(str(k))
    return (a if a == -1 else a+1)        