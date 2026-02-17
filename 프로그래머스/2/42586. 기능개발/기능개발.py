##기능 개발
#stack, queue
def solution(progresses, speeds):
    #1. 일단 맨 앞에꺼 100이 나올때까지 더해야함.
    #2. 100이 나오면, progresses에서 100이 이어진 수만큼 answer에 추가,
    #3. 100이 연속적으로 나온 것들의 인덱스를 찾아 progresses, speeds에서 지움
    
    answer = []
    valid_check = 0
    while len(progresses)>=1:
        
        #일단 더하기
        for i in range(len(progresses)):
            if progresses[i] + speeds[i] >= 100:
                progresses[i] = 100
            else:
                progresses[i] += speeds[i]
        valid_check += 1
        # print("횟수:{0}, progresses:{1}".format(valid_check, progresses))
        
        #맨 앞에가 100을 달성했을때
        if progresses[0] == 100:
            stack = 1
            
            # print("제일 앞이 100 달성! 이때 progresses:{}".format(progresses))
            
            #제일 앞의 progresses 지우기
            progresses.pop(0)
            speeds.pop(0)
            while True:
                #progresses의 요소가 남아있고, 그 다음 요소가 100일때
                if len(progresses) > 0 and progresses[0] == 100:
                    stack += 1
                    progresses.pop(0)
                    speeds.pop(0)
                #아니면 break
                else:
                    break
            answer.append(stack)
    return answer