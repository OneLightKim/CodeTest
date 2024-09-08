def solution(numbers):
#     temp1,temp2 = [],[]
#     for i in numbers:
#         if i<0:
#             temp2.append(i)
#         elif i>=0:
#             temp1.append(i)
#     print(temp1)
#     print(temp2)

#     if len(temp1)>=2:
#         a1 = max(temp1)
#         temp1.remove(a1)
#         a11 = max(temp1)
#         a_temp1 = a1*a11
#     else:
#         a_temp1 = 0

#     if len(temp2)>=2:
#         a2 = min(temp2)
#         temp2.remove(a2)
#         a22 = min(temp2)
#         a_temp2 = a2*a22
#     else:
#         a_temp2 = 0

#     if a_temp1>a_temp2:
#         answer = a_temp1
#     else:
#         answer = a_temp2
    # temp_down, temp_up = [], []
    # n=1
    # for i in numbers:
    #     if i <= 0:
    #         temp_down.append(i)
    #     elif i>0:
    #         temp_up.append(i)
    # if len(temp_down)>=2:
    #     a = min(temp_down)
    #     temp_down.remove(a)
    #     b = min(temp_down)
    #     down = a*b
    # elif len(temp_up)>=2:
    #     c = max(temp_up)
    #     temp_up.remove(c)
    #     d = max(temp_up)
    #     up = c*d
    # else:
    #     for i in numbers:
    #         n *= i
    # if down>up:
    #     return down
    # elif down<up:
    #     return up
    # else:
    #     return up
    numbers.sort(reverse = True)
    return max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])