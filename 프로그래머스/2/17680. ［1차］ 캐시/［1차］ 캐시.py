##1차 캐시
#LRU알고리즘?: 가장 오랫동안 사용되지 않았던 데이터부터 버린다
    #캐시는 크기가 제한되어있어, 새 데이터를 넣으려면, 기존 데이터를 지워야 할 때가 있는데,
    #이때 가장 오래된 데이터를 지우는 방법이 LRU(Least Recently Used)
#cache hit, miss?: 찾으려는 도시가 cache에 있으면, "hit" 없으면 "miss"
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    temp_cache = []
    
    #1. !추가
    cities = [x.lower() for x in cities]
    
    #2. !추가
    if cacheSize == 0:
        return len(cities) * 5
    
    #3. !추가. deque (pop보다 시간 복잡도 낮음. remove, append사용 등)
    cache = deque(maxlen=cacheSize)
    
    #루프
    for city in cities:
        if city in cache: #hit
            answer += 1
            cache.remove(city)
            cache.append(city)
            # print(cache)
        else:                       #miss
            answer += 5
            cache.append(city)
            # print(cache)
            
    return answer