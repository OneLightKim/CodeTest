##연속 부분 수열 합의 개수
#Sliding window
def solution(elements):
    answer = set()
    elements = elements * 2
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)
"""
elements를 두배로 곱해 놓으면 되는 거였음.
"""