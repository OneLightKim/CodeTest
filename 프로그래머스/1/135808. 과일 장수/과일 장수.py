# def solution(k, m, score):
#     answer = 0
#     #k값 이상 모두 제거
#     for index in range(len(score)):
#         if score[index] > k:
#             score.remove(score[index])
#     #내림차순 정렬 후, 수행할 횟수 정하기
#     score.sort(reverse=True)
#     num = (len(score)//m)*m
#     #앞 부터 차례대로 m개만큼 추가, 인덱스가 m까지 왔으면, answer에 min값을 추가
#     arr = [] #빈 배열
#     for index in range(num):
#         arr.append(score[index])
#         if (index+1)%m == 0:
#             answer += min(arr)*m
#             arr = []
#     return answer



def solution(k,m,score):
    #즉, 한 상자에 사과를 m개 담을 수 있는데
    #가장 낮은 점수를 가지는 사과*m*상자 개수 해서 가장 높은 Score를 구한다.
    #k는 가장 높은 점수를 가지는 사과의 점수로 제약사항임.
    #그러면 핵심은? 정렬을 하고, 낮은거는 낮은 것 끼리, 높은거는 높은 것 끼리 모으는게 맞을 듯
    sorted_score = [i for i in sorted(score, reverse=True) if i<=k]
    answer = 0
    for i in range(len(sorted_score)//m):
        answer += min(sorted_score[i*m:i*m+m])*m
    return answer
    

