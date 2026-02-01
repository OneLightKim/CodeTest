from itertools import combinations
def solution(k, tangerine):
    answer = 0
    #각 크기의 귤을 세고, key, value로 넣기
    tan_dict = {}
    for i in tangerine:
        if i in tan_dict:
            tan_dict[i] += 1
        else:
            tan_dict[i] = 1
    
    #최대한 적은 key의 value의 합으로 k 만들기
    #한 종류의 귤의 개수가 k개를 넘어도 괜찮! 다 안넣으면 되니깐.
    #그래서 내림차순으로. 이 코드는, dict를 value를 기준으로 내림차순 정렬해주는 것
        #items()하면, ('1',1)이런 형태로 되는데, key = lambda x: x[1]이면, 1을 기준으로 내림차순 정렬해달라는게 됨.
    tan_dict = dict(sorted(tan_dict.items(), key = lambda x:x[1], reverse = True))
    
    for key, value in tan_dict.items():
        if k<= 0:
            return answer
        k -= value
        answer += 1
        
        
    
    return answer