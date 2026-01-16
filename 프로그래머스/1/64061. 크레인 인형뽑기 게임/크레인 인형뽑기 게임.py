#크레인 인형뽑기 게임
#아! 0은 빈칸이고, 번호는 열이었네.
def solution(board, moves):
    answer = 0
    #이중 리스트 구조임.
    #열 기준으로 특정 숫자를 뽑게 되면, 바구니에 아래부터 쌓임
        #이중 리스트의 제일 끝의 행부터 뽑는거임
        #바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 큼
    #같은게 두개 쌓이면 사라짐.
    #0은 빈칸이며, 인형이 없는 곳에서 크레인을 작동시키면 아무 일도 일어나지 않음.
    
    #인형을 바구니로, 이중 리스트에서는 뽑은 인형 제거
    basket = []
    for move in moves:
        #비어 있지 않은 행 찾기
        i = 0
        while True:
            if board[i][move-1] != 0:
                break
            #5행 밖으로 나가면 끝이니깐
            elif i+1 == len(board):
                i = len(board)-1
                break
            i += 1
        #만약 move열의 모든 행이 비어있다면 pass
        if board[i][move-1] == 0:
            pass
        #basket에 인형 담기, 비어있는 칸으로
        else:
            basket.append(board[i][move-1])
            board[i][move-1] = 0
        
        #바구니에 인형을 담았을 때 바로 전 인형이 같은 인형이라면, 제거하고 answer += 1
        if len(basket) > 1 and basket[-2] == basket[-1]:
            del basket[-2:]
            answer += 2
    return answer