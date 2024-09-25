def solution(array):
    temp = {}
    for i in array:
        if i not in temp:
            temp[i] = 1
        elif i in temp:
            temp[i] += 1
    max_num = max(temp.values())

    #최대값 value 개수 계산
    count = 0
    for i in temp:
        if temp[i]==max_num:
            count += 1
    #최대값 value가 여러개면 -1을
    if count > 1:
        return -1
    #value값에 해당하는 Key값 반환
    else:
        for i,j in temp.items():
            if j == max_num:
                return i