##가장 많이 받은 선물

def solution(friends, gifts):
    answer = 0
    ##규칙
    #이번 달까지 A,B가 서로 주고 받은 선물 수 중 A가 준 선물이 더 많을 때 A가 B에게 하나 더 받음
    #이번 달까지 A,B가 주고받은 기록이 없거나, 주고 받은 선물 수가 같다면, "선물 지수"가 더 큰 사람이 작은 사람에게 하나 받음.
        #선물지수: 친구들에게 준 선물 수 - 친구들에게 받은 선물 수
    #answer는 다음달에 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶은 것
    
    #friends 만큼의 열과 행을 가지는 초기 행렬 선언.
    gives = [[0 for j in range(len(friends))] for i in range(len(friends))]
    #준 선물 수를 채워 넣기
    for gift in gifts:
        temp = gift.split(' ')
        gives[friends.index(temp[0])][friends.index(temp[1])] += 1
    
    print('gives\n',gives)
    
    #각 페어의 경우의 수 계산
    #계산 이전 각자의 선물 지수를 계산
    indicator = {}
    for i in range(len(gives)):
        give_num = sum(gives[i])
        receive_num = 0
        for j in range(len(gives[i])):
            receive_num += gives[j][i]
        indicator[friends[i]] = give_num-receive_num
    print('indicator\n',indicator)
    
    #다음 달 각자 받을 선물의 수 선언
    receive_dict = {friend:0 for friend in friends}

    #각 페어의 경우의 수 계산
    for i in range(len(gives)):
        for j in range(len(gives[i])):
            #같은 사람 비교는 pass
            if i==j:
                print('pass',i,j)
                pass
            #1. 한쪽이 더 많이 준 경우
            elif gives[i][j] > gives[j][i]:
                print(friends[j],'give to', friends[i])
                receive_dict[friends[i]] += 1
            elif gives[i][j] < gives[j][i]:
                print(friends[i],'give to', friends[j])
                receive_dict[friends[j]] += 1
            #2. 같거나, 서로 안 준 경우 -> 선물 지수 수로 승부
            elif gives[i][j] == gives[j][i]:
                if indicator[friends[i]] > indicator[friends[j]]:
                    print('in same situation', friends[i],'give to', friends[j])
                    receive_dict[friends[i]] += 1
                elif indicator[friends[i]] < indicator[friends[j]]:
                    print('in same situation', friends[j],'give to', friends[i])
                    receive_dict[friends[j]] += 1
                else:
                    pass
    print('receive_dict',receive_dict)
    
    #receive_dict에서 가장 큰 value를 answer로 반환
    answer = max(receive_dict.values())//2
    
    return answer
