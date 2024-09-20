def solution(my_string):
    """my_list = my_string.split(" ")
    for i in my_list:
        if i == '+':
            my_list.remove('+')
            count = 0
        elif i == '-':
            my_list.remove('-')
            count = 1
    my_list = list(map(int,my_list))
    if count == 0:
        return sum(my_list)
    else:
        return my_list[0] - my_list[1]"""
    return eval(my_string)