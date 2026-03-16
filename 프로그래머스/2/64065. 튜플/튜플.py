def solution(s):
    answer = []
    #일단 리스트 형태로
    a = []
    b = ''
    b_list = []
    for i in s:
        if i.isdigit():
            b += i
            # print(b)
        elif i==',' and len(b)>0:
            b_list.append(int(b))
            b = ''
            # print(',',b_list)
        elif i=='}' and len(b)>0:
            b_list.append(int(b))
            a.append(b_list)
            b = ''
            b_list = []
            
    # print('a',a)
    
    #길이 순 정렬
    a.sort(key=len)
    
    #set안의 원소 중 answer에 없는게 있다면 추가하기
    for raw in a:
        for i in raw:
            if i not in answer:
                answer.append(i)
                
    return answer