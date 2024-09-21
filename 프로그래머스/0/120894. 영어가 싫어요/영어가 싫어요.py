def solution(numbers):
    # for i,j in zip(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],[
    #     '0','1','2','3','4','5','6','7','8','9'
    # ]):
    #     if i in numbers:
    #         numbers = numbers.replace(i,j)
    dict_num = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    for i,j in dict_num.items():
        numbers = numbers.replace(i,j)
    return int(numbers)