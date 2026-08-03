# def solution(participant, completion):
#     hash_dict = {}
#     for p in participant:
#         if p in hash_dict:
#             hash_dict[p] += 1
#         else:
#             hash_dict[p] = 1
#     for p in completion:
#         hash_dict[p] -= 1
#     for key, value in hash_dict.items():
#         if value > 0:
#             return key


def solution(participant, completion):
    h_dict = {}
    for p in participant:
        if p not in h_dict:
            h_dict[p] = 0
        h_dict[p] += 1
    for c in completion:
        if c in h_dict.keys():
            h_dict[c] -= 1
    for key, value in h_dict.items():
        if value > 0:
            return key
        
        
        