##피로도
#완전탐색 -> 백트래킹(DFS를 이용한)
def solution(k, dungeons):
    global visited, answer
    answer = 0
    visited = [False for i in range(len(dungeons))]
    dfs(k,0,dungeons)
    return answer
        
#dfs의 작동을 완전히 외워두자.
#일단 아이디어는 1->2->3 방문이 안되니, 다시 1로 돌아가서 1->3->2방문을 선택.
    #DFS순열 등으로 모든 경우의 수 탐색
    #조건문을 걸어 답이 될 수 없는 상황 정의
    #그런 상황에서 탐색 중지 -> 이전으로 돌아가 다른 경우의 수 탐색
def dfs(k, cnt, dungeons):
    global answer
    #cnt란 현재 탐색 경로에서 지금까지 방문한 던전 수
    if cnt > answer:
        answer = cnt
    for i in range(len(dungeons)):
        #방문 하지 않고, 필요피로도보다 k가 크거나 같은 경우
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True #지금 경로에서는 해당 dungeon을 써버렸다는 것.
            # print(visited, k)
            dfs(k-dungeons[i][1], cnt+1, dungeons) #그 상태로 다음 던전을 찾아 깊게 들어감.
            visited[i] = False #이제 방금 길은 다 확인했으니, 아까 이 던전을 방문하기 전 상태로 되돌려 놓는다.