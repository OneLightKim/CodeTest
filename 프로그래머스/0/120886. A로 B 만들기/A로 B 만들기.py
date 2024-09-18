# def solution(before, after):
#     after_dict = {}
#     before_dict = {}
#     answer = 1
#     for i in after:
#         after_dict[i] = 0
#     for j in before:
#         before_dict[j] = 0
#     for i in after:
#         after_dict[i] += 1
#     for j in before:
#         before_dict[j] += 1
#     for a,b in after_dict.items():
#         if b != before_dict[a]:
#             answer = 0
#     return answer
def solution(before, after):
    after_dict = {}
    before_dict = {}
    answer = 1

    for i in after:
        after_dict[i] = 0
    for j in before:
        before_dict[j] = 0

    for i in after:
        after_dict[i] += 1
    for j in before:
        before_dict[j] += 1

    for a, b in after_dict.items():
        if b != before_dict.get(a, 0):  # before_dict에 a가 없으면 0 반환
            answer = 0

    return answer
