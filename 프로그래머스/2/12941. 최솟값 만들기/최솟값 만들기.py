##최솟값 만들기
def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    for i in range(len(A)):
        answer += A[0] * B[-1]
        del A[0]
        del B[-1]

    return answer