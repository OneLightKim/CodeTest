def solution(strings, n):
    answer = []
    temp_list = []
    for i in range(len(strings)):
        temp_list.append(strings[i][n] + strings[i])
    temp_list.sort()
    print(temp_list)
    for j in range(len(temp_list)):
        answer.append(temp_list[j][1:])
    return answer