#이 답도 맞긴한데,, 왜 틀리게 뜨지
# def solution(common):
#     answer = 0
#     x = common[1] // common[0]
#     print(x)
#     if common[0]+1 == common[1]:
#         answer = common[-1]+1
#     elif common[0] * x == common[1]:
#         answer = common[-1]*x
#     return answer
def solution(common):
    answer = 0
    d = common[1] - common[0]
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + d
    else:
        r = common[1] / common[0]
        if common[1] / common[0] == common[2] / common[1]:
            answer = common[-1] * r
    return answer