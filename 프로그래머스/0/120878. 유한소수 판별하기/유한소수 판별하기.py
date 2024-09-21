def solution(a, b):
    #1. 기약분수로 나타내기
    n,m=1,1
    list_a = []
    list_b = []
    while a>=n:
        if a%n==0:
            list_a.append(n)
        n += 1
    while b>=m:
        if b%m==0:
            list_b.append(m)
        m += 1

    equal_num = []
    for i in list_a:
        if i in list_b:
            equal_num.append(i)
    a,b = int(a/max(equal_num)), int(b/max(equal_num))
    
    #2. 2또는 5로 나뉘어지면 1, 아니면0
    while b%2==0:
        b //= 2
    while b%5==0:
        b //= 5
    if b==1:
        return 1
    else:
        return 2
    