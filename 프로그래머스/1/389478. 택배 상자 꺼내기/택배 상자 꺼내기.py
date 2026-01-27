import math
def solution(n, w, num):
    answer = 1
    #1. 먼저, (n/w)*w 빈 리스트 생성
    array = [[0 for j in range(w)] for i in range(math.ceil(n/w))]
    
    #2. array의 마지막부터 차례차례 상자 쌓기.
    side = 1 #왼쪽, 오른쪽 판단용.
    row = -1 #초기 행 인덱스
    b = 1 #채워넣기
    for i in range(math.ceil(n/w)):
        if side%2 != 0: #왼쪽에서 오른쪽
            for j in range(w):
                if b > n:
                    pass
                else:
                    array[row][j] = b
                    b += 1
    
        elif side%2 == 0: #오른쪽에서 왼쪽
            for j in range(w-1,-1, -1):
                if b > n:
                    pass
                else:
                    array[row][j] = b
                    b += 1
        row -= 1 #윗 행으로
        side += 1 #방향 전환
    print(array)
    #3. 상자 꺼내기
    #우선 num의 인덱스를 찾아야함. (행과 열)
    num_row = math.ceil(num/w) #행 (끝에서 몇 번째인지)
    num_col = array[-num_row].index(num) # 열 (검사 시에는 행 인덱스에 -를)
    
    #상자 꺼내기
    for i in range(len(array)-num_row):
        if array[i][num_col] != 0:
            answer += 1
        else:
            pass
    
    return answer