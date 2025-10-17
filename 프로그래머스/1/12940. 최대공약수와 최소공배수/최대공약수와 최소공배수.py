# def solution(n, m):
#     #최대 공약수 구하기
#     answer = []
#     n_f,m_f = [],[]
#     for i in range(1, n+1):
#         if n%i==0:
#             n_f.append(i)
#     for i in range(1, m+1):
#         if m%i==0:
#             m_f.append(i)
#     f = max(list(set(n_f).intersection(set(m_f))))
#     answer.append(f)
#     #최대 공배수 구하기
#     for i in range(max(n,m),n*m+1):
#         if n%i==0 and m%i==0:
#             answer.append(i)
#             break
#     return answer

def solution(n, m):
    answer = []
    n_f,m_f = [],[]
    
    # 최대공약수
    for i in range(1, n+1):
        if n%i==0:
            n_f.append(i)
    for i in range(1, m+1):
        if m%i==0:
            m_f.append(i)
    f = max(set(n_f).intersection(set(m_f)))
    answer.append(f)
    
    # 최소공배수
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer