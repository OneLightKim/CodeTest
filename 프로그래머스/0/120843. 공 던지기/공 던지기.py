def solution(numbers, k):
    count,num = 0,0
    while True:
        count += 1
        if count == k:
            return numbers[num]
            break
        num += 2
        if num>len(numbers):
            num = num-len(numbers)
