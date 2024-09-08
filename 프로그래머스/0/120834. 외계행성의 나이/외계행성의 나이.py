def solution(age):
    answer = ''
    new_age = list(map(int,str(age)))
    for i in new_age:
        answer += chr(i+ord('a'))
    return answer