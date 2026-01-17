def solution(numbers, hand):
    #양손 엄지를 움직여 숫자 배열을 입력한다.
        #양손 시작은 *, #
        #한칸당 거리1
        #오른손잡이, 왼손잡이
        
        #무조건 1,4,7은 왼손, 3,6,9는 오른손
        #가까운손이 2,5,8,0 입력(현재 위치를 알 수 있어야할듯)
        #같은 거리라면 왼손, 오른손잡이에 따라 갈림
    answer = ''
    
    # 1. 좌표 만들기
    arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left_finger = [3,0]
    right_finger = [3,2]
    
    # 2. numbers 루프
    for num in numbers:
        get_pos = []
        for i,row in enumerate(arr):
            try:
                j = row.index(num)
                get_pos.append(i)
                get_pos.append(j)
            except:
                pass
        
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left_finger[0], left_finger[1] = get_pos[0], get_pos[1]
            print('Left')
        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            right_finger[0], right_finger[1] = get_pos[0], get_pos[1]
            print('right')
        else:
            #왼, 오 손가락부터 target의 거리 구하기
            left_dis = abs(left_finger[0]-get_pos[0]) + abs(left_finger[1]-get_pos[1])
            right_dis = abs(right_finger[0]-get_pos[0]) + abs(right_finger[1]-get_pos[1])
            print('ld, rd: {0}, {1}'.format(left_dis, right_dis))

            #왼, 오 손가락 고르기, 좌표 저장
            if left_dis > right_dis:
                answer += 'R'
                right_finger[0], right_finger[1] = get_pos[0], get_pos[1]
            elif left_dis < right_dis:
                answer += 'L'
                left_finger[0], left_finger[1] = get_pos[0], get_pos[1]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_finger[0], right_finger[1] = get_pos[0], get_pos[1]
                else:
                    answer += 'L'
                    left_finger[0], left_finger[1] = get_pos[0], get_pos[1]
                                    
    # 현재 왼,오 손가락의 좌표 저장
    # 눌러야할 버튼의 좌표 찾기
    
    return answer