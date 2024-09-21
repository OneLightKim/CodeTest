def solution(keyinput, board):
    """
    코드가 비 효율적이었다.
    answer = [0,0]
    for i in keyinput:
        if i=='left':
            answer[0]=answer[0]-1
        elif i=='right':
            answer[0]=answer[0]+1
        elif i=='up':
            answer[1]=answer[1]+1
        elif i=='down':
            answer[1]=answer[1]-1
    if answer[0]>(board[0]-1)//2:
        answer[0]=(board[0]-1)//2
    elif answer[0]<-(board[0]-1)//2:
        answer[0]=-(board[0]-1)//2
    elif answer[1]>(board[1]-1)//2:
        answer[1]=(board[1]-1)//2
    elif answer[1]<-(board[1]-1)//2:
        answer[1]=-(board[1]-1)//2
    아래는 더 효율적인 코드이다. 효율적인 코드의 if and를 앞으로 사용하도록 하자    
    """
    answer = [0, 0]
    
    x = board[0] // 2
    y = board[1] // 2
    
    for i in keyinput:
        if i == "up" and answer[1]+1 <= y:
            answer[1] += 1
        elif i == "down" and answer[1]-1 >= -y:
            answer[1] -= 1
        elif i == "left" and answer[0]-1 >= -x:
            answer[0] -= 1
        elif i == "right" and answer[0]+1 <= x:
            answer[0] += 1
    return answer