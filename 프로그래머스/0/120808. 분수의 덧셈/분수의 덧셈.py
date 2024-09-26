def solution(numer1, denom1, numer2, denom2):
    answer = []
    top,under = numer1*denom2+numer2*denom1,denom1*denom2
    top_list = [i for i in range(1, top + 1) if top % i == 0]
    under_list = [i for i in range(1, under + 1) if under % i == 0]
    same = [i for i in top_list if i in under_list]
    answer.append(top//max(same))
    answer.append(under//max(same))
    
    

    return answer