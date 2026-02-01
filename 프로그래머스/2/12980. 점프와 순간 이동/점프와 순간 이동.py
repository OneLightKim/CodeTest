##점프와 순간 이동
#사실 이 문제는 n을 이진수로 만들었을 때 '1'의 개수를 세는 것 과 같음.
def solution(n):
    ans = 0
    while n > 0:
        if n%2 == 0:
            n //= 2
        else:
            ans += 1
            n -= 1

    return ans