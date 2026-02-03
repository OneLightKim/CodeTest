##예상 대진표
def solution(n,a,b):
    answer = 1
    if a > b:
        a,b = b,a
    while True:
        if b-1 == a and b//2 -1 == a//2:
            # print("둘은 만낫다. a: {0}, b:{1}".format(a,b))
            break
        
        if a%2 == 0:
            # print("a",a)
            a //= 2
        else:
            # print("a",a)
            a //= 2
            a += 1
            
        if b%2 == 0:
            # print('b',b)
            b //= 2
        else:
            # print('b',b)
            b //= 2
            b += 1
        answer += 1
    return answer
