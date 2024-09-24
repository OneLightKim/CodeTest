# def solution(A, B):
#     """
#     #코드1. 효율적이지 않음
#     if A==B:
#         return 0
#     A,B = list(A),list(B)
#     a = 0
#     while a<=len(A)-1:
#         answer = []
#         for i in range(len(A)-1):
#             answer.append(A[i])
#         answer.insert(0,A[-1])
#         if answer == B:
#             return 1
#         A = answer
#         a += 1
#     return -1"""
#     if A == B:
#         return 0
#     for i in range(1, len(A) + 1):
#         # A를 오른쪽으로 한 칸씩 밀어서 B와 비교
#         if A[-i:] + A[:-i] == B:
#             return 1
#     return -1

from collections import deque

def solution(A, B):
    Alist = deque(A) # 데크
    Blist = deque(B) # 데크
    for i in range(len(Alist)):
        if Alist == Blist: # A와 B가 같아지면 이동 횟수 i 리턴
            return i
        Alist.rotate(1) # 오른쪽으로 1칸 이동
    return -1 # 불가능한 경우 -1 리턴