##연속 부분 수열 합의 개수
#Sliding window
def solution(elements):
    answer = set()
    #길이가 전체가 아닐 때에는 그냥 길이만큼 반복문이 도나?
        # O
    
    elements = elements*2
    for i in range(len(elements)//2):
        #마지막의 경우 그냥 elements 전체 더해버리기
        for j in range(len(elements)//2):
            # index out of range를 해결할 방법? 그냥 elements두배 하면 되는 일. 
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)
"""
elements를 두배로 곱해 놓으면 되는 거였음.
"""