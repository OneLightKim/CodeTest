def solution(num, total):
    temp = []
    a = 0
    while True:
        if a==0:
            temp.append(a)
        else:
            temp.append(a)
            temp.append(-a)
        print(temp)
        if len(temp)>=num:
            if total == sum(temp[-num:]):
                return temp[-num:]
        a += 1
        
def solution(num,total):
    #등차수열의 합 공식 (num*(num-1)/2)사용...
    #근데 이제 시작점x를 곁들인.
    #x를 초기로 가지는 Num개의 숫자 개수 합은 x + (x+1) + ...(x+(num-1))임. 이것은 Total
    #즉 total = num*x + (num*(num-1)/2)로 가능
    x = (total - (num * (num - 1)) // 2) // num
    answer = [x+i for i in range(num)]
    return answer