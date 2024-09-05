def solution(numbers):
    answer = 0
    a = max(numbers)
    numbers.remove(max(numbers))
    b = max(numbers)
    answer = a*b
    return answer