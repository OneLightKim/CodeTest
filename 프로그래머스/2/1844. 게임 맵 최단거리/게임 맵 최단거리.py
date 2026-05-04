from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0,0,1)) #x,y좌표 및 현재까지 이동한 거리
    
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    while q:
        x,y,dist = q.popleft() #현재 위치 및 거리를 x,y,dist 변수에 저장
        
        if x == n-1 and y == m-1: #popleft한게 마지막 지점에 도달했다면
            return dist #이동한 거리를 반환
        
        for dx, dy in [(1,0),(-1,0), (0,1), (0,-1)]: #현재 위치에서 상,하,좌,우로 이동하기
            nx, ny = x+dx, y+dy
            
            if 0<=nx<n and 0<=ny<m: #nx, ny가 맵 범위 안에 있는 좌표냐? 를 묻는거임
                if maps[nx][ny] == 1 and not visited[nx][ny]: #그 좌표가 1이라면
                    visited[nx][ny] = True #방문했음 표시하고
                    q.append((nx, ny, dist+1)) #큐에 append 
                    # print("현재 deque:",q) #print찍어보니 현재 좌표가 1인 것들은 q에 append가 모두 되고 그 다음에 popleft하여 검증하는 것임. 그래서 모든 분기를 체크함. 근데,,, 뒤로 가는 경우도 포함하게 될텐데 괜찮나 이거? -> visited가 True로 체크되니 이전것으로는 안 돌아가겠네.
                                          #그러니깐, 다른 분기점의 경로로 가더라도 visited가 체크되어있으니까 다른데로 새어나갈 염려를 안해도 되는 것임
                    
    return -1
                