def solution(k, m, score):
    answer = 0
    #k값 이상 모두 제거
    for index in range(len(score)):
        if score[index] > k:
            score.remove(score[index])
    #내림차순 정렬 후, 수행할 횟수 정하기
    score.sort(reverse=True)
    num = (len(score)//m)*m
    #앞 부터 차례대로 m개만큼 추가, 인덱스가 m까지 왔으면, answer에 min값을 추가
    arr = [] #빈 배열
    for index in range(num):
        arr.append(score[index])
        if (index+1)%m == 0:
            answer += min(arr)*m
            arr = []
    return answer