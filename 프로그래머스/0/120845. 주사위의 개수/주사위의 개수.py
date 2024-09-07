def solution(box, n):
    for i in box:
        globals()[f'n_{i}'] = i//n
    answer = 1
    for j in range(1,4):
        answer *= globals()[f'n_{i}']
    return answer