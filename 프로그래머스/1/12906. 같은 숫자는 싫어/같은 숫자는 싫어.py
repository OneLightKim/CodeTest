# def solution(arr):
#     i = 0
#     while i < len(arr)-1:
#         if arr[i] == arr[i + 1]:
#             arr.pop(i + 1)
#         else:
#             i += 1
#     return arr

# def solution(arr):
#     ans = [arr[0]]
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i-1]:
#             ans.append(arr[i])
#     return ans

# def solution(arr):
#     ans = [arr[0]]
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i-1]:
#             ans.append(arr[i])
#     return ans


def solution(arr):
    arr_0 = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr_0.append(arr[i])
    return arr_0

