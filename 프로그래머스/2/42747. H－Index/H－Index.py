def solution(citations):
    citations.sort(reverse=True)
    #발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상
    for idx, val in enumerate(citations):
        #논문 개수가 인용 횟수보다 커지는 순간을 찾는 것
        if idx+1 > val:
            # print(idx+1, val)
            return idx
    return len(citations)