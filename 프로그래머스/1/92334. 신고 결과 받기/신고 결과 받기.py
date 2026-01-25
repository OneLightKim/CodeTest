#신고 결과 받기
def solution(id_list, report, k):
    # report의 0은 신고자, report의 1은 신고 당하는 유저.
    
    # 1. 각 유저가 신고 당한 횟수
    dict_id_list = {i:0 for i in id_list} #초기화
    
    # 2. 각 유저가 특정 유저를 신고한 횟수
    report = [r.split(' ') for r in report] #report읽기 편하게
    count_id_list = [[0 for _ in range(len(id_list))] for _ in range(len(id_list))]
    
    #3. 신고 횟수 누적시키기
    for i in range(len(report)):
        if count_id_list[id_list.index(report[i][0])][id_list.index(report[i][1])] < 1:
            dict_id_list[report[i][1]] += 1
            count_id_list[id_list.index(report[i][0])][id_list.index(report[i][1])] += 1
    # print(dict_id_list)
    # print(count_id_list)
    
    
    #4. 각 유저가 정지를 성공시킨 유저 수 세기
    answer = [0 for i in range(len(id_list))]
    for i in range(len(count_id_list)):
        for j in range(len(count_id_list[i])):
            if count_id_list[i][j] == 1 and dict_id_list[id_list[j]] >= k:
                answer[i] += 1
                
    
                    
    
    return answer