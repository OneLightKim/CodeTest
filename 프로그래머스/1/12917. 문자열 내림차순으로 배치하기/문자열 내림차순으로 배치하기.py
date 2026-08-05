# def solution(s):
#     return ''.join(sorted(s, reverse=True))


def solution(s):
    answer = ''.join(sorted(s, reverse=True)) #sorted는 항상 리스트로 반환함. 그래서 join이 필요. 근데, 정수들은 결합이 안되니, 결합을 하려하면 map으로 str로 바꾸고 결합하도록 강제해야함
    return answer