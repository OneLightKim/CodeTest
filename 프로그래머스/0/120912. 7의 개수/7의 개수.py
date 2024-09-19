def solution(array):
    temp = []
    for i in array:
        temp.append(str(i))
    temp = ''.join(temp)
    answer = temp.count('7')
    return answer