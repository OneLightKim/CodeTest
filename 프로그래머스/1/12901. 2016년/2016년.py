#2016년

def solution(a,b):
    day = {0:"FRI",1:"SAT",2:"SUN",3:"MON",4:"TUE",5:"WED",6:"THU"}
    month = list(range(1, a+1))
    days = b-1
    days_num = 0
    if len(month) == 1:
            return day[days%7]
    for i in range(len(month)-1):
        if month[i] in (1,3,5,7,8,10,12):
            days_num += 31
        elif month[i] in (4,6,9,11):
            days_num += 30
        else:
            days_num += 29
    return day[(days_num+days)%7]
    