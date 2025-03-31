# def solution(n):
#     list_n=[]
#     for i in range(1,n+1):
#         if n%i==0:
#             list_n.append(i)
#         else:
#             pass
#     x = 1
#     for i in list_n:
#         if isinstance(i,int):
#             x *= i
#         else:
#             pass
            
#     return x

def solution(n):
    x = 0
    for i in range(1,n+1):
        if n%i == 0:
            x += i
    return x