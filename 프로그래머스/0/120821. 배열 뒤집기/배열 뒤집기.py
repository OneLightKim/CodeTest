def solution(num_list):
    answer = []
    for i in range(len(num_list)//2):
        num_list[i],num_list[-(i+1)] = num_list[-(i+1)],num_list[i]
        
    return num_list