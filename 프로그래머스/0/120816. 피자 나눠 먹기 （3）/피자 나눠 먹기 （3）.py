def solution(slice, n):
    a = n // slice
    if n % slice > 0:
        a += 1
    
    return a