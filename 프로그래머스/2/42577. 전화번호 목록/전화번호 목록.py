def solution(phone_book):
    hash_map = set(phone_book)
    
    #이거는, 해당하는 넘버의 일부가 다른 곳에 접두사로 포함되는지 체크하는 것임
    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_number[:i] in hash_map:
                return False
    return True