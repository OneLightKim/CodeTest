def solution(n, m, section):
    section_set = set(section)        # ✅ 수정 1
    temp_section = section_set
    temp_drawed = set()
    drawed = []
    count = 0

    for i in range(1, n+1):            # ✅ 수정 2 (sector 제거)
        if i in section_set and i not in temp_drawed:
            paint_range = range(i, i + m)
            drawed.extend(paint_range)
            temp_drawed.update(paint_range)
            count += 1
            if temp_section.issubset(temp_drawed):
                return count

    return count