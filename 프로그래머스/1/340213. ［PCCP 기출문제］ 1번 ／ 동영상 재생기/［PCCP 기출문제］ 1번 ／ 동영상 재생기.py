#[PCCP 기출문제] 1번 / 동영상 재생기
#자료형, if문과의 싸움
def solution(video_len, pos, op_start, op_end, commands):
    #prev명령어 시 10초 전으로, 현재 위치가 10초 미만 -> 처음으로(0분0초)
    #next명령어 시 10초 후로, 현재 위치가 끝에서 10초 미만이라면, 영상의 마지막 위치로
    #오프닝 건너뛰기 시 (오프닝 구간에 있어야함)오프닝이 끝나는 위치로 이동
        #next시 opening이 겹치면 뛰어넘기
    current = [i for i in pos.split(':')]
    video_len = [i for i in video_len.split(':')]
    op_start, op_end = [i for i in op_start.split(':')], [i for i in op_end.split(':')]
    print(current, video_len, op_start, op_end)
    print(current)
    for command in commands:
        #현재가 오프닝 구간이라면 -> 오프닝 끝
        if int(current[0]+current[1]) <= int(op_end[0]+op_end[1]) and int(current[0]+current[1]) >= int(op_start[0]+op_start[1]):
            current[0], current[1] = op_end[0], str(int(op_end[1]))
            print('current opening')
            #current의 형식 다시 맞추기
            if len(str(current[0]))<2:
                current[0] = '0' + str(current[0])
            if len(str(current[1]))<2:
                current[1] = '0' + str(current[1])
            print(current)
        
        #next시
        if command == 'next':
            #(2 수행을 위해 임시 리스트 마련)
            print('next')
            print(current)
            temp = []
            temp.append(int(current[0]))
            temp.append(int(current[1]))
            temp[1] += 10
            #temp에 분, 초 규칙 적용
            if temp[1] >= 60:
                temp[1] -= 60
                temp[1] = str(temp[1])
                temp[0] += 1
                temp[0] = str(temp[0])
            if len(str(temp[0]))<2:
                temp[0] = '0' + str(temp[0])
            if len(str(temp[1]))<2:
                temp[1] = '0' + str(temp[1])
            temp[0], temp[1] = str(temp[0]), str(temp[1])
            
            
            #2. 10초 후가 오프닝 구간에 있다면 -> 오프닝 끝
            if int(temp[0]+temp[1]) < int(op_end[0]+op_end[1]) and int(temp[0]+temp[1]) >= int(op_start[0]+op_start[1]):
                current[0], current[1] = op_end[0], op_end[1]
                print('next 10 is opening')
            else:
                print(current[1])
                current[1] = int(current[1])+10
                current[1] = str(current[1])
                print('default')
                print(current)
            
            #3. next에 맞는 분, 초 규칙 적용
            if int(current[1]) >= 60:
                current[1] = int(current[1])-60
                current[1] = str(current[1])
                current[0] = int(current[0])+1
                current[0] = str(current[0])
                
            #4. 10 초 후가 video_len 초과 시 video_len과 동일 
            if int(current[0]) >= int(video_len[0]) and int(current[1]) > int(video_len[1]):
                current[0], current[1] = video_len[0], video_len[1]
            
            #5. current의 형식 다시 맞추기
            if len(str(current[0]))<2:
                current[0] = '0' + str(current[0])
            if len(str(current[1]))<2:
                current[1] = '0' + str(current[1])
            
        #prev 시    
        elif command == 'prev':
            print('prev')
            #0. 빼기
            current[1] = int(current[1])-10
            print(current)
            #1. prev에 맞는 분, 초 규칙 적용
            if current[1] < 0:
                current[1] += 60
                current[0] = int(current[0])-1
            
            #2. 10초 전이 보다 작으면 0으로
            if int(current[0]) < 0:
                current[0], current[1] = '00', '00'
            
            current[0], current[1] = str(current[0]), str(current[1])
            
            #current의 형식 다시 맞추기
            #3. current의 형식 다시 맞추기
            if len(str(current[0]))<2:
                current[0] = '0' + str(current[0])
            if len(str(current[1]))<2:
                current[1] = '0' + str(current[1])
            
            #4. prev했는데 opening이라면
            if int(current[0]+current[1]) < int(op_end[0]+op_end[1]) and int(current[0]+current[1]) >= int(op_start[0]+op_start[1]):
                current[0], current[1] = op_end[0], op_end[1]
    #규칙 맞추기
    answer = current[0] + ':' + current[1]
    return answer