def solution(s):
    answer = True
    count1, count2 = 0,0
    len_s = len(s)
    for i in s:
        if i.lower() == 'p':
            count1 += 1
        elif i.lower() == 'y':
            count2 += 1
    if count1 == count2:
        return True
    else:
        return False