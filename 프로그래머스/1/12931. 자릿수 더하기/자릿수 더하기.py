def solution(n):
    answer = 0
    n_str = str(n)
    num_len = len(n_str)
    for i in range(1,num_len+1):
        digit = (n//(10**(num_len-i))) %10
        answer += digit
    return answer