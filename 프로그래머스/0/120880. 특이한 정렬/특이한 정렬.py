def solution(numlist, n):
    # numlist = [1, 2, 3, 4, 5, 6]
    # n = 4

    answer = []
    #1. numlist에서 n을 뺀 값들과 그 값들의 abs를 반환.
    temp = [i-n for i in numlist]
    temp_2 = list(map(abs,temp))
    temp_3 = sorted(list(set(temp_2)))

    # print('temp',temp)
    # print('temp2',temp_2)
    # print('temp3',temp_3,'\n')

    #2. 같은 인덱스에 위치한 값들이 temp_2에서 같으면 
    ## 큰 값의 인덱스에 해당하는 num_list에 먼저 넣고 작은 값은 그 다음에 넣기
    for i in temp_3:
        temp_temp = []
        # print("temp_3",i)
        #temp_3값과 같은 temp2의 값의 index에 해당하는 temp값을 temptemp에 넣는것이 목표
        count = 0
        for j in temp_2:
            if i == j:
                #여기에서 해당하는 인덱스의 temp값을 넣지 못하는 문제
                # print(temp_2.index(j))
                temp_temp.append(temp[count])
                # temp_2.remove(temp_2[temp_2.index(j)])
            count += 1
        # print(temp_temp)
        # 해당하는 값이 2개라면 같은 차이에 해당하는 numlist값 중 큰값을 먼저 append
        if len(temp_temp) == 2:
            answer.append(numlist[temp.index(max(temp_temp))])
            answer.append(numlist[temp.index(min(temp_temp))])
        # 해당하는 값이 1개라면 해당하는(numlist-n)값을 answer에 할당
        else:
            answer.append(numlist[temp_2.index(i)])

    return answer