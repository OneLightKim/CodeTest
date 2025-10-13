def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    list_num = list(set(num)-set(numbers))
    a = 0
    for i in range(len(list_num)):
        a += list_num[i]
    return a