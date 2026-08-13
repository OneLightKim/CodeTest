##프로세스
#!!스택은 후입선출, queue는 선입선출
# from collections import deque
# def solution(priorities, location):
#     #deque사용(선입선출) 그러니깐.. index0에 있는게 제일 먼저 넣은거임.
#         #popleft, append만 쓰면됨
#     #일단 꺼냄
#         #대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣음
#         #만약 그런 프로세스 없다면 방금 꺼낸 프로세스를 그대로 실행
#         #한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료
#     answer = 0
#     #deque에 tuple형태로 인덱스와 함께 value를 넣기(dict보다 튜플이 빠름)
#     dq = deque()
#     for i,v in enumerate(priorities):
#         # deque({i:k}) dict로 넣는다면 이렇게
#         dq.append((i,v))
    
#     #문제 수행
#     i = 0
#     while dq:
#         # q = dq.popleft()
#         # if q[1] == max(priorities) and q[0] == location:
#         #     answer += 1
#         #     return answer
#         # elif q[1] == max(priorities):
#         #     del priorities[i]
#         #     answer += 1
#         # else:
#         #     dq.append(q)
#         # i += 1
#         q = dq.popleft()
#         #가장 높은 우선순위가 아니면 다시 넣기
#         if dq and max(item[1] for item in dq)>q[1]:
#             dq.append(q)
#         else:
#             answer += 1
#             if q[0] == location:
#                 return answer
#     return answer


from collections import deque

def solution(priorities, location):
    dq = deque()
    for i,v in enumerate(priorities):
        dq.append((i,v))
        
    answer = 0
    while dq:
        q = dq.popleft()
        if dq and max(item[1] for item in dq) > q[1]:
            dq.append(q)
        else:
            answer += 1
            if q[0] == location:
                return answer