# def solution(word):
#     count = 0
#     found = [False]
#     result = [0]
#     def dfs(current_s):
#         nonlocal count
#         if current_s != '':
#             count +=1
#         if len(current_s) >= 5:
#             return
#         if found[0]:
#             return
#         if current_s == word:
#             found[0] = True
#             result[0] = count
#             return
#         for c in ['A', 'E', 'I', 'O', 'U']:
#             dfs(current_s+c)
#     dfs('')
#     return result[0]

##모음사전
#DFS
#재귀를 배웠다.
#리턴할 경우가 많아 어려웠다.
#초반에 아이디어 구상을 못했다.
#다른 방법으로 풀어봐야한다.
def solution(word):
    answer = 0
    found = [False]
    result = [0]
    def dfs(current_s):
        nonlocal answer
        if found[0]: #부모 함수의 for 루프가 다음 형제 자식을 호출하려 할 때, 그 호출을 즉시 무력화시켜 부모 함수도 빨리 끝나게 만드는 장치
            return
        if current_s != '': #비어있지 않다면 count +=1
            answer +=1
        if current_s == word: #정답이라면 result에 count 저장, 찾았다! -> 부모로
            result[0] = answer
            found[0] = True
            return
        if len(current_s) >= 5: #5이면 부모 함수로 가서 for문 돌리기
            return
        for c in ['A','E','I','O','U']:
            dfs(current_s + c)
    dfs('')
    return result[0]