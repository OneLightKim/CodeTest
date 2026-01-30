##완전탐색/카펫
def solution(brown, yellow):
    #방정식 써서 풀면 됨!
    """
    xy = yellow
    brown = 2(x+2)+2y
    """
    for x in range(1,int(yellow**(1/2)+1)):
        if yellow%x == 0:
            y = yellow//x
            
            if 2*x + 2*y + 4 == brown:
                x += 2
                y += 2
                return [max(x,y), min(x,y)]
