# def solution(n, lost, reserve):
#     #1. 여벌 있는데 도난당항 학생들은 양쪽 명단에서 삭제
#     real_reserve = set(reserve) - set(lost)
#     real_lost = set(lost) - set(reserve)
    
#     #2. 다시 리스트로, 작은 번호부터 정렬되도록
#     real_reserve = sorted(list(real_reserve))
#     real_lost = sorted(list(real_lost))
    
#     #3. 초기 answer
#     answer = n - len(real_lost)
    
#     #4. 도난 당한 학생 빌려주기
#     for l in real_lost:
#         if l - 1 in real_reserve:
#             real_reserve.remove(l - 1)
#             answer += 1
#         elif l + 1 in real_reserve:
#             real_reserve.remove(l + 1)
#             answer += 1
                
#     return answer




def solution(n,lost,reserve):
    #여벌의 체육복을 가진 학생들은, 바로 앞 뒤 학생에게만 빌려줄 수 있으며, 체육복은 최대 2개임
    #여벌 체육복을 가진 학생도 도난을 당할 수 있음.
    #체육복을 받아 체육수업을 들을 수 있는 최대 학생 수를 리턴
    #이거는, 일단 가지고 있는 체육복 수를 체크하는게 맞을 듯
    get_dict = {}
    for i in range(n):
        get_dict[i] = 1
        if i+1 in lost:
            get_dict[i] -= 1
        if i+1 in reserve:
            get_dict[i] += 1
    
    for i in range(n):
        if get_dict[i] == 0:
            if i-1 >= 0 and get_dict[i-1] == 2:
                get_dict[i] += 1
                get_dict[i-1] -= 1
            elif i+1 < n and get_dict[i+1] == 2:
                get_dict[i] += 1
                get_dict[i+1] -= 1
    answer = 0
    for key, value in get_dict.items():
        if value >= 1:
            answer += 1
    return answer
        
        
    