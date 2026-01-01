#기사단원의 무기 시간 복잡도 줄이기

def solution(number, limit, power):
    #number까지의 배열로
    nums = list(range(1,number+1))
    #각 기사의 공격력을 배정
    power_list = []
    for i in nums:
        count = 0
        for j in range(1, int(i**(1/2))+1):
            if i%j==0:
                count += 1
                if j**2 != i:
                    count += 1
        if count > limit:
            power_list.append(power)
        else:
            power_list.append(count)
    return sum(power_list)