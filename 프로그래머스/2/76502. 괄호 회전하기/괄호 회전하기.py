##괄호 회전하기
#조건문 잘 짜는 문제임..
#로직이 다수 틀림 -> 간소화 해보자(if문에 괄호 여러개는 인정) ㄴㄴㄴㄴㄴㄴ
#올바른 괄호 형식을 생각하자 -> stack
    #왜냐하면 [(])가 틀린 것을 고려 안함.
def solution(s):
    #문자열을 길이만큼 왼쪽으로 밀기
        #왼쪽으로 미는 기술 필요
        #0번째 요소를 빼서 append하면 될 듯?
    #괄호가 올바르게 닫혔는지 확인 필요
        #[ { (
    
    answer = 0
    correct = {']':'[', '}':'{', ')':'('}
    arr = list(s)
    
    #왼쪽으로 밀기
    for i in range(len(arr)):
        #[,{,(로 시작하는지
        if arr[0] not in list(correct.values()):
            pass
        else:
            stack = []
            for j in range(len(arr)):
                #열린 괄호는 무조건 추가
                if arr[j] in list(correct.values()):
                    stack.append(arr[j])
                #닫힌 괄호 추가 시
                #1. stack의 arr[j-1]이 닫힌괄호 같으면 stack[-1]을 없애기, 추가 안하기. 
                #2. 1번이 아니라면, break
                else:
                    if len(stack) == 0:
                        break
                    elif stack[-1] == correct[arr[j]]:
                        del stack[-1]
                    else:
                        break
            #무사히 끝났으면, 괄호 페어가 맞는지 확인
            else:
                if len(stack)==0:
                    answer += 1
        # print(arr)
        arr.append(arr.pop(0))
    return answer