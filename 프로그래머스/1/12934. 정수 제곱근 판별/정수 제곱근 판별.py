# def solution(n):
#     answer = 0
#     num = 0
#     for i in range(1,n+1):
#         if n/i == i and n%i == 0:
#             num = i
#             break
#         else:
#             pass
#     answer = (num+1)*(num+1)
#     return answer


def solution(n):
    if int(n**0.5) == n**0.5:
        return int(((n**0.5)+1)**2)
    else:
        return -1