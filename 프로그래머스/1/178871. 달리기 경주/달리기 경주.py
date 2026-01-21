#달리기경주
#시간복잡도 줄이기
def solution(players, callings):
    #dict에 초기 등수를 저장
    result = {player:i for i, player in enumerate(players)}
    for who in callings:
        #인덱스를 불러올때애 dict에서 불러오기
        idx = result[who]
        #dict의 인덱스를 바꾸기
        result[who] -= 1
        result[players[idx-1]] += 1
        #players를 그 인덱스로 수정
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players