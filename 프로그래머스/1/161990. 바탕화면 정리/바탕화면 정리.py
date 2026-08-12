# #바탕화면 정리
# def solution(wallpaper):
#     answer = [-1,-1,-1,-1]
#     #최소 시작점, 최소 끝점 좌표를 반환
#     #빈 공간은 '.', 채워진 공간은 '#'
#     #최소 행, 최소 열 찾기
#     for i in range(len(wallpaper)):
#         for j in range(len(wallpaper[i])):
#             #최소 행 채우기 및 초기 값 채워넣기
#             if wallpaper[i][j] == '#' and answer[0] == -1:
#                 answer[0], answer[2] = i, i
#                 answer[1], answer[3] = j, j
#             #최소 열 추가
#             if wallpaper[i][j]=='#' and answer[1] > j:
#                 answer[1] = j
#             #끝행,열 추가
#             if wallpaper[i][j]=='#' and answer[2] < i:
#                 answer[2] = i
#             if wallpaper[i][j]=='#' and answer[3] < j:
#                 answer[3] = j
#     answer[2] += 1
#     answer[3] += 1
#     return answer



def solution(wallpaper):
    idx = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=="#":
                idx.append((i,j))
    height = [x[0] for x in idx]
    width = [x[1] for x in idx]
    return [min(height), min(width), max(height)+1, max(width)+1]
    
            
        