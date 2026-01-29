##숫자의표현
def solution(n):
    answer = 0
    s = 1
    while s<=n:
        num = 0
        # arr = []
        for i in range(s, n+1):
            num += i
            # arr.append(i)
            if num == n:
                answer += 1
                # print(arr)
                break
            elif num > n:
                # print(num)
                break
        s += 1
    return answer