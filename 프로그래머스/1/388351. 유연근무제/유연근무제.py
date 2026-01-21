#유연근무제

def solution(schedules, timelogs, startday):
    answer = 0
    #각자 설정한 출근 시간에 일주일동안 늦지 않고 타임로그를 남겨야함.
        #1,2,3,4,5,6,7순으로 월-일이며, 6,7일 경우 늦어도됨.
        #한번이라도 실패하지 않으면 answer에 1을 더하자.
    
    #schedules의 목표 출근 시간 +10하여 알맞은 기준으로
    schedules = [s+50 if (s+10)%100 >= 60 else s+10 for s in schedules]
    print("new_schedules: {}".format(schedules))
    
    #timelogs와 schedules비교
    for i in range(len(schedules)):
        count = 0
        day = startday 
        for j in range(len(timelogs[i])):
            # print("day: {}".format(day))
            if day not in [6,7]:
                if schedules[i] >= timelogs[i][j]:
                    pass
                else:
                    count += 1
                    # print("실패!")
                    break
            day += 1
            if day > 7:
                day = 1
            else:
                pass
        if count == 0:
            answer += 1
        
    return answer
