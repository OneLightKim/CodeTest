#성격 유형 검사하기

def solution(survey, choices):
    #RT, CF, JM, AN
    #4개의 문자가 합쳐진 문자열이 결과로 나오게됨.
    #문항들과 그 점수를 담은 배열이 제공됨
    
    #점수 테이블
        #1-3 왼쪽의 요소
        #4   사전 순의 왼쪽의 요소
        #5-7 오른쪽의 요소
        
        #7,1점은 각각 3점
        #6,2점은 각각 2점
        #5,3점은 각각 1점
        #4점은 점수 없음
    
    #RT, TR, CF, FC, JM, MJ, AN, NA
    #만약 둘의 점수 합이 0이라면 사전순으로 앞에있는 문자를
    answer = ''
    
    
    #점수 저장 테이블 선언
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    #점수 파싱
    for s, c in zip(survey, choices):
        if c == 1:
            score[s[0]] += 3
        elif c == 2:
            score[s[0]] += 2
        elif c == 3:
            score[s[0]] += 1
        elif c == 5:
            score[s[1]] += 1
        elif c == 6:
            score[s[1]] += 2
        elif c == 7:
            score[s[1]] += 3
        else:
            pass
        
    #문자열 출력
    symbol = list(score.keys())
    for i in range(0,len(symbol),2):
        if score[symbol[i]] > score[symbol[i+1]]:
            answer += symbol[i]
        elif score[symbol[i]] < score[symbol[i+1]]:
            answer += symbol[i+1]
        else:
            answer += symbol[i]
            
    return answer