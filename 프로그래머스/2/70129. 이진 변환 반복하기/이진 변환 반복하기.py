##이진 변환 반복하기
def solution(s):
    answer = []
    #0을 제거
    #2진 변환
    count_num = 1 #마지막 2진 변환 결과 초기값
    zero_count = 0
    while True:
        zero_count += s.count('0')
        s = s.strip('0')
        binary = 0 #이진 변환할 것 초기화
        for i in s:
            binary += int(i)
        s = str(bin(binary))[2:]
        # print('s:',s)
        if s == '1':
            break
        else:
            count_num += 1
    answer = [count_num, zero_count]
    return answer