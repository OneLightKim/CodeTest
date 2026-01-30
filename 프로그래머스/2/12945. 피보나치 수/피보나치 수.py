##피보나치 수
def solution(n):
    temp = [0,1]
    for i in range(2, n+1):
        temp.append(temp[i-2]+temp[i-1])
        # print(temp)
    return temp[-1]%1234567