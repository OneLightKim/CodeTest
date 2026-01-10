def solution(dartResult):
    calc_list = []
    i = 0
    while i < len(dartResult):
        # 1. 숫자 파싱
        num = ""
        while i < len(dartResult) and dartResult[i].isdigit():
            num += dartResult[i]
            i += 1
        
        # 2. 보너스 처리 (S, D, T)
        # 숫자를 읽은 직후에는 반드시 S, D, T 중 하나가 옵니다.
        if i < len(dartResult):
            char = dartResult[i]
            if char == "S":
                calc_list.append(f"({num}**1)")
            elif char == "D":
                calc_list.append(f"({num}**2)")
            elif char == "T":
                calc_list.append(f"({num}**3)")
            i += 1 # 보너스 문자 처리했으므로 인덱스 이동

        # 3. 옵션 처리 (*, #) - 없을 수도 있으므로 체크
        if i < len(dartResult):
            if dartResult[i] == "*":
                # 현재(마지막) 점수 2배
                calc_list[-1] = f"({calc_list[-1]}*2)"
                # "직전" 점수가 있다면 그것만 2배 (전체 X)
                if len(calc_list) >= 2:
                    calc_list[-2] = f"({calc_list[-2]}*2)"
                i += 1
            elif dartResult[i] == "#":
                # 현재 점수만 마이너스
                calc_list[-1] = f"({calc_list[-1]}*(-1))"
                i += 1
                
    # 최종 수식 합치기
    answer = eval('+'.join(calc_list))
    return answer