# def solution(arr):
#     answer = 0
#     arr_len = len(arr)
#     for i in arr:
#         answer += i
#     answer = answer/arr_len
#     return answer


def solution(arr):
    answer = sum(arr)/len(arr)
    return answer