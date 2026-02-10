##행렬의 곱셈
def solution(arr1, arr2):
    #arr1 = A*B
    #arr2 = B*C
    #arr1*arr2 = A*C
    result = []
    for i in range(len(arr1)):          #arr1의 행
        row = []
        for j in range(len(arr2[0])):   #arr2의 열
            total = 0
            for k in range(len(arr2)):  #arr2의 행 = arr1의 열
                total += arr1[i][k] * arr2[k][j]
            row.append(total)
        result.append(row)
    return result