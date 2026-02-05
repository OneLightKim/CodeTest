##할인행사
def solution(want, number, discount):
    
    #상품, 수량 dict구성
    want_num = {}
    for i,j in zip(want, number):
        want_num[i] = j

    result = []
    #시작 날짜
    for i in range(len(discount)-9):

        #want_num초기화
        want_num1 = want_num.copy()

        #10일동안의 날짜
        for j in range(i, i+10):
            if discount[j] in want_num1.keys():
                want_num1[discount[j]] -= 1
        #10일 동안 원하는 상품과 수량을 모두 구매 가능한지
        count = 0
        for key,value in want_num1.items():
            if value <= 0:
                count += 1
        if count == len(want_num1):
            result.append(i)
    
    return len(result)