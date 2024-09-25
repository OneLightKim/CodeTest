##원래 코드. 답은 올바르게 나오지만, split함수를 쓰지 않아
# def solution(polynomial):
#     answer = ''
#     count = 0
#     num = 0
#     for i in range(len(polynomial)):
#         #x개수 더하기
#         if polynomial[i]=='x':
#             if polynomial[i-1].isdigit():
#                 count += int(polynomial[i-1])
#             else:
#                 count += 1
#         elif polynomial[i].isdigit():
#             print('숫자만',polynomial[i])
#             if polynomial[i+1]==' ':
#                 num += int(polynomial[i])
#     if num != 0:
#         answer += f'{count}x' + f' + {num}'
#     else:
#         answer += f'{count}x'
#     return answer

def solution(polynomial):
    count = 0  # x합
    num = 0  # 상수합
    terms = polynomial.split(' + ')
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                count += 1
            else:  #x앞 숫자 처리
                count += int(term.replace('x', ''))
        # 상수
        else:
            num += int(term)

    #결과 반환
    result = []
    if count == 1:
        result.append('x')  #x가 1이면 x로만
    elif count > 1:
        result.append(f'{count}x')
    if num > 0:
        result.append(f'{num}')
    
    return ' + '.join(result)
