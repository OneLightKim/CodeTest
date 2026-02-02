##N개의 최소공배수
def solution(arr):
    #arr을 먼저 sort
    #젤 작은거 두개 최소 공배수 찾고, sort
    #이거를 한개 남을때까지
    while len(arr) > 1:
        arr.sort()
        # print('검사 전 arr',arr)
        for i in range(max(arr[0],arr[1]), (arr[0]*arr[1])+1):
            if i%arr[0] == 0 and i%arr[1] == 0:
                del arr[0]
                del arr[0]
                arr.append(i)
                # print('공배수 찾은 후 arr',arr)
                break
    return arr[0]