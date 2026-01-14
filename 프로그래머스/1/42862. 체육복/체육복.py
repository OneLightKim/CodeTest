def solution(n, lost, reserve):
    # 1. 중복 제거 (여벌 있는데 도난당한 애들은 양쪽 명단에서 삭제)
    # set을 쓰면 자동으로 정렬되지 않으므로 나중에 list로 변환 및 정렬 필요
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    
    # 2. set을 list로 바꾸고 정렬 (작은 번호부터 처리해야 최적)
    real_reserve = sorted(list(real_reserve))
    real_lost = sorted(list(real_lost))
    
    # 3. 진짜 잃어버린 학생 수만큼 일단 빼고 시작 (체육복 있는 학생 수)
    answer = n - len(real_lost)
    
    # 4. 빌려주기 로직
    for l in real_lost:
        if l - 1 in real_reserve:
            real_reserve.remove(l - 1)
            answer += 1
        elif l + 1 in real_reserve:
            real_reserve.remove(l + 1)
            answer += 1
            
    return answer