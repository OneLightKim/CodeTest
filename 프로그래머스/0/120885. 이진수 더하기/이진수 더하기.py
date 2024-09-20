def solution(bin1, bin2):
    # answer = ''
    # #1. list로
    # bin1, bin2 = list(bin1), list(bin2)
    # #2. 마지막 요소 (-1)값이 1이라면 1로, 0이라면 0
    # sum_bin1, sum_bin2 = 0,0
    # for i in range(1, len(bin1)+1):
    #     if int(bin1[-i]) == 0:
    #         pass
    #     #3. 그 다음 요소 의 abs값-1을 2의 제곱하도록
    #     if int(bin1[-i]) == 1:
    #         sum_bin1 += 2**(abs(i)-1)
    # for i in range(1, len(bin2)+1):
    #     if int(bin2[-i]) == 0:
    #         pass
    #     #3. 그 다음 요소 의 abs값-1을 2의 제곱하도록
    #     if int(bin2[-i]) == 1:
    #         sum_bin2 += 2**(abs(i)-1)
    # bin1,bin2 = int(bin1),int(bin2)
    bin1,bin2 = int(bin1,2), int(bin2,2)
    return str(bin(bin1+bin2)[2:])