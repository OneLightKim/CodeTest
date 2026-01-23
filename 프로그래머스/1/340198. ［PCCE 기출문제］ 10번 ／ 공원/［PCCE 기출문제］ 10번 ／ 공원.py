#[PCCE 기출문제] 10번 / 공원
#mats를 sort
#5중포문
#early stop
def solution(mats, park):
    answer = 0
    # 필 수 있는 가장 큰 돗자리를 구해야함.
    # mat * mat로 구할 수 있는 곳 끝까지 구해야할듯

    mats.sort(reverse=True)
    
    for mat in mats:
        #index가 초과되지 않게, mat길이만큼
        for r in range(len(park)-mat+1):
            for c in range(len(park[r])-mat+1):
                count = 0
                for i in range(mat):
                    for j in range(mat):
                        if park[r+i][c+j] != '-1':
                            count += 1
                            break
                    else:
                        continue
                    break
                if count == 0:
                    return mat
            
    return -1