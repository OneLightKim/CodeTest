def solution(quiz):
    answer = []
    for strings in quiz:
        strings = strings.split('=')
        if eval(strings[0]) != int(strings[1]):
            answer.append("X")
        else:
            answer.append("O")
    return answer