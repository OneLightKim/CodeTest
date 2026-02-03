##영어 끝말잇기
#문제 중 한 로직이 틀려서 고치는 중
def solution(n, words):
    #1-n까지의 번호가 있는 사람이 영어 끝말잇기를 함.
    #끝말잇기 규칙
        #1. 1번부터 번호 순서대로 차례대로 단어를 말함
        #2. 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작
        #3. 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야함.
        #4. 이전에 등장했던 단어는 못 사용
        #5. 한 글자인 단어는 인정 X
    #만약 이전에 말했던 단어라면 탈락
    #탈락하는 사람의 번호와 몇 번째 차례에 탈락하는지 길이 2의 배열을 return
    
    
    temp = []
    for i in range(1,len(words)):
        #탈락하는 경우의 수1. 다른 알파벳으로 시작할 때
        if words[i-1][-1] != words[i][0]:
            temp.append(i%n + 1)
            temp.append(i//n + 1)
            return temp
        #탈락하는 경우의 수2. 이미 등장한 word를 또 언급했을 때 
        elif words[i-1] in words[:i-1]:
            temp.append((i-1)%n + 1) #차례
            temp.append((i-1)//n + 1) #반복횟수
            return temp
        elif words[i] in words[:i]:
            temp.append(i%n + 1) #차례
            temp.append(i//n + 1) #반복횟수
            return temp
        
    return [0,0]