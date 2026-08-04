# def solution(s):
#     a, b = 0, 0
#     for i in s:
#         if i == '(':
#             a += 1
#         elif i == ')' and a == 0:
#             return False
#         elif i == ')' and a != 0:
#             b += 1
#         if b > a:
#             return False
#     if a == b:
#         return True
#     else:
#         return False






def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    else:
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0 