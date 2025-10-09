# def solution(n):
#     answer = 0
#     n_str = str(n)
#     num_len = len(n_str)
#     for i in range(1,num_len+1):
#         digit = (n//(10**(num_len-i))) %10
#         answer += digit
#     return answer


# def solution(n):
#     answer = 0
#     n_str = str(n)
#     num_len = len(n_str)
#     print(num_len)
#     print()
#     answer = 0
#     for i in range(1,num_len+1):
#         answer += n//(10**(num_len-i))
#         n -= (10**(num_len-i))*(n//(10**(num_len-i))%10)
        
#         print(f"몫 answer: {answer}")
#         print(f"자리값 answer*(10**(num_len-i)): {answer*(10**(num_len-i))}")
#         print(f"n:{n}")
#     return answer
# solution(123)

def solution(n):
    sum=0
    while n>0:
        sum += n%10
        n //= 10
    return sum