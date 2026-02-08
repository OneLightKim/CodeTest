##n^2 배열 자르기 
#시간 초과
#또 시간 초과
def solution(n, left, right):
    answer = []
    #그냥 배열 만들기로
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)
    
    return answer
