def solution(n, arr1, arr2):
    answer = []
    arr1_b = []
    arr2_b = []
    #각 리스트를 이진수로
    for num in arr1:
        arr1_b.append(str(format(num,'b').zfill(n)))
    for num in arr2:
        arr2_b.append(str(format(num,'b').zfill(n)))
    print(arr1_b, arr2_b)
    #각 이진수를 합치기
    for i in range(len(arr1_b)):
        for j in range(len(arr1_b[i])):
            if arr1_b[i][j] == '0' and arr2_b[i][j] == '1':
                print(arr1_b[i][:j])
                arr1_b[i] = arr1_b[i][:j]+'1'+arr1_b[i][j+1:]
    #각 이진수에서 1을 #, 0을 ' '으로
    for i in range(len(arr1_b)):
        for j in range(len(arr1_b[i])):
            if arr1_b[i][j] == '1':
                arr1_b[i] = arr1_b[i][:j]+'#'+arr1_b[i][j+1:]
            else: 
                arr1_b[i] = arr1_b[i][:j]+' '+arr1_b[i][j+1:]
    return arr1_b