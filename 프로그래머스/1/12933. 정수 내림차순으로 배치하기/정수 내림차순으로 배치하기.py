def solution(n):
    list_n = sorted(map(int, str(n)), reverse=True)
    answer = ''.join(map(str,list_n))
    return int(answer)
solution(12345)