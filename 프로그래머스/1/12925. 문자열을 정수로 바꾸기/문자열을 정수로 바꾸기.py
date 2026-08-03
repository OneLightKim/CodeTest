# def solution(s):
#     result = 0
#     for idx, number in enumerate(s[::-1]):
#         if number == '-':
#             result *= -1
#         else:
#             result += int(number) * (10**idx)
        
#     return result



def solution(s):
    S = list(s)
    n = 1
    for i in range(len(S)):
        if S[i] == '-':
            del S[i]
            n = -1
            break
    return int(''.join(S))*n
            