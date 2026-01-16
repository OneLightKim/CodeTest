def solution(data, ext, val_ext, sort_by):
    """data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순 정렬
    단, 조건을 만족하는 데이터는 항상 한 개 이상 존재함.
    ext, sort_by는 "code", "date", "maximum", "remain"값 중 하나로 주어짐"""
    answer = []
    #1. ext 미만만 남기기
    if ext == "code":
        for arr in data:
            if arr[0] < val_ext:
                answer.append(arr)
    elif ext == "date":
        for arr in data:
            if arr[1] < val_ext:
                answer.append(arr)
    elif ext == "maximum":
        for arr in data:
            if arr[2] < val_ext:
                answer.append(arr)
    elif ext == "remain":
        for arr in data:
            if arr[3] < val_ext:
                answer.append(arr)
    
    #2. sort_by를 기준으로 sort
    if sort_by == "code":
        answer.sort(key = lambda x:x[0])
    elif sort_by == "date":
        answer.sort(key = lambda x:x[1])
    elif sort_by == "maximum":
        answer.sort(key = lambda x:x[2])
    elif sort_by == "remain":
        answer.sort(key = lambda x:x[3])
    
    return answer