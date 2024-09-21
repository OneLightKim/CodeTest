def solution(dots):
    dots_x = [dots[i][0] for i in range(len(dots))]
    dots_x = max(dots_x)-min(dots_x)
    dots_y = [dots[i][1] for i in range(len(dots))]
    dots_y = max(dots_y)-min(dots_y)
    return dots_x*dots_y