#공원 산책
def solution(park, routes):
    #route에서 표시한 각 요소만큼 이동 후 마지막 좌표를.
        #루트로 갈 때애 1. 장애물에 막혀있거나, 2. 공원 길이를 초과하면
        #다음 루트로
        
    #시작 좌표 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                answer = [i,j]
                break
            else:
                continue #안쪽 포문이 break업이 끝낫다면 진행
            break #아니면 끝
    # print(answer)
        
    #좌표 움직이기 시작. 동-서-남-북 순으로
    for route in routes:
        route = route.split(' ')
        route[1] = int(route[1])
        if route[0] == 'E':
            if len(park[0]) >= answer[1]+route[1]+1:
                if 'X' not in park[answer[0]][answer[1]:answer[1]+route[1]+1]:
                    answer[1] += route[1]
            else:
                pass
        elif route[0] == 'W':
            if answer[1]-route[1] > -1:
                if 'X' not in park[answer[0]][answer[1]-route[1]:answer[1]+1]:
                    answer[1] -= route[1]
        elif route[0] == 'S':
            if len(park) >= answer[0]+route[1]+1:
                count=0
                # print('answer, len(park): {0}, {1}'.format(answer, len(park)))
                for i in range(answer[0],answer[0]+route[1]+1):
                    # print(park[i][answer[1]])
                    if park[i][answer[1]] == 'X':
                        count += 1
                        break
                if count == 0:
                    answer[0] += route[1]
        elif route[0] == 'N':
            if answer[0]-route[1] >= 0:
                count = 0
                for i in range(answer[0], answer[0]-route[1]-1, -1):
                    if park[i][answer[1]] == 'X':
                        count += 1
                        break
                if count == 0:
                    answer[0] -= route[1]
                    
    
    return answer