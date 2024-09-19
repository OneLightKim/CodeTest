def solution(s):
    answer = ''
    temp = list(s)
    temp_list = []
    for i in temp:
        if temp.count(i)<=1:
            temp_list.append(i)
    answer = ''.join(sorted(temp_list))
    return answer