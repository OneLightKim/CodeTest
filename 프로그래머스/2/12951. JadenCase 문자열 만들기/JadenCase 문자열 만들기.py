def solution(s):
    temp = []
    for i in s.split(' '):
        temp.append(i.capitalize())
    answer = ' '.join(temp)
    return answer