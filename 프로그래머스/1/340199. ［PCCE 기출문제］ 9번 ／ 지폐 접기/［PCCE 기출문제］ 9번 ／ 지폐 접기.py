#지폐 접기
def solution(wallet, bill):
    answer = 0
    #bill의 작은 값이 wallet의 작은 값 보다 크거나, bill의 큰 값이 wallet의 큰 값 보다 큰 동안 반복
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        if bill[0] > bill[1]:
            bill[0] = bill[0]//2
            answer += 1
            if wallet[0] > wallet[1] and bill[0] < bill[1]:
                bill.sort(reverse=True)
            elif wallet[0] < wallet[1] and bill[0] > bill[1]:
                bill.sort()
                
        else:
            bill[1] = bill[1]//2
            answer += 1
            if wallet[0] > wallet[1] and bill[0] < bill[1]:
                bill.sort(reverse=True)
            elif wallet[0] < wallet[1] and bill[0] > bill[1]:
                bill.sort()
    return answer