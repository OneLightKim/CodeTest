# def solution(array, n):
    # answer = 0
    # temp = []
    # for i in array:
    #     temp.append(abs(i-n))
    # answer = array[temp.index(min(temp))]
"""    answer = array[0]
    min_diff = abs(array[0] - n)

    for i in array:
        diff = abs(i - n)
        if diff < min_diff:
            min_diff = diff
            answer = i"""
    # return answer

def solution(array, n):
    box = []
    array.sort()
    for i in array:
        box.append(abs(n-i))
    answer = [array[box.index(min(box))]]
    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]