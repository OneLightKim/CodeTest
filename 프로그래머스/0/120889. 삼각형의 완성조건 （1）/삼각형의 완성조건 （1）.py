def solution(sides):
    # answer = 0
    # a = max(sides)
    # sides.remove(a)
    # l = 0
    # for i in sides:
    #     l += i
    # if l >= a:
    #     answer=1
    # else:
    #     answer=2
    # return answer
    spare = sum(sides)-max(sides)
    if max(sides) >= spare:
        answer = 2
    else:
        answer = 1
    return answer