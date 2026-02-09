def solution(clothes):
    dict = {}
    for cloth in clothes:
        if cloth[1] not in list(dict.keys()):
            dict[cloth[1]] = 1
        else:
            dict[cloth[1]] += 1
    #각 value를 1씩 더해 answer에 곱해주는게 경우의 수임. 
    #마지막에 남는 1의 경우 아무것도 안 입는 경우이니, 이것을 뺴 줘야함.
    answer = 1
    for key, value in dict.items():
        answer *= value+1
    return answer-1