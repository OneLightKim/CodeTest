def solution(people, limit):
    answer = 0
    people.sort()  # 정렬: [50, 50, 70, 80]
    
    # 투 포인터 초기화
    left = 0                 # 가장 가벼운 사람의 위치 (맨 왼쪽)
    right = len(people) - 1  # 가장 무거운 사람의 위치 (맨 오른쪽)
    
    # 두 포인터가 교차할 때까지 (즉, 모든 사람을 태울 때까지)
    while left <= right:
        # 가장 무거운 사람(right)과 가장 가벼운 사람(left)이 같이 탈 수 있나?
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람 탑승 처리 (화살표를 오른쪽으로 한 칸 이동)
        
        # 무거운 사람은 짝이 있든 없든 무조건 탑승
        right -= 1     # 무거운 사람 탑승 처리 (화살표를 왼쪽으로 한 칸 이동)
        
        # 보트 하나 출발
        answer += 1
        
    return answer