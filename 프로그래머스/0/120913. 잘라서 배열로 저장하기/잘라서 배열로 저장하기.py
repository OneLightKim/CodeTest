def solution(my_str, n):
    answer = []
    # for i in range(len(my_str)//n+1):
    #     answer.append(my_str[i*n:(i+1)*n])
            # my_str = my_str.replace(my_str[i*6:(i+1)*6],'')
    # for i in range(0,len(my_str),6):
    #     answer.append(my_str[i:i*n])
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer