def solution(score):
    answer = []
    for i in range(len(score)):
        answer.append(sum(score[i])/2)
    temp = sorted(answer,reverse=True)
    return [temp.index(i)+1 for i in answer]