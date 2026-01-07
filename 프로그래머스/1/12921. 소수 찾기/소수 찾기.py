#소수 찾기
#시간 복잡도 줄인 버전
def solution(n):
    answer = 0
    for num in range(2,n+1):
        for i in range(2,int(num**(1/2)+1)):
            if num%i == 0:
                break
        else:
            answer += 1
    return answer