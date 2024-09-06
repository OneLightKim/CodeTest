def solution(array):
    answer = []
    big = max(array)
    idx = array.index(big)
    answer.extend([big,idx])
    return answer