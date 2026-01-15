#숫자 짝꿍
#시간초과, 논리오류..(실패 경우와 0만 있는 경우를 고려 안했잖아. 문제 똑바로 보자.)
def solution(X, Y):
    answer = ''
    
######################################################## 이 부분이 잘못된거임. 시간 복잡도 너무 높아
    #새로운 방법! 9부터 하나씩 세며 공통된 숫자 개수 만큼 answer에 추가 
    for i in range(9,-1,-1):
        num = str(i)
        count_x = X.count(num)
        count_y = Y.count(num)
        min_count = min(count_x, count_y)
        answer += num*min_count
    #실패 경우 1
    if answer == '':
        return '-1'
    #실패 경우 2
    elif len(answer) > 1 and answer[0] == '0':
        return '0'
    return answer
########################################################
#     #3. 실패 경우(추가)
#     if len(common) == 0:
#         return '-1'
#     elif max(common) == 0 and len(common) > 1:
#         return '0'
    
#     #4. list에서 가장 큰 수를 빼서 answer에 넣기
#     i = 0
#     for i in range(len(common)):
#         answer += str(max(common))
#         common.pop(common.index(max(common)))
        
#     return answer