import re
def solution(new_id):
    answer = ''
    #새로 가입 유저 아이디 추천
    #아이디 규칙에 맞지 않는 아이디 입력 시 입력된 아이디와 유사하며 규칙에 맞는 아이디 추천
    #3-15자 | 알파벳 소문자, 숫자, -, _, . 문자만 사용 가능.
        #'.'는 처음과 끝에 사용할 수 없으며 연속으로 사용 불가능
    
    #1. new_id의 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()
    # print("step1 new_id: {}".format(new_id))
    #2. new_id에서 알파벳 소문자, 숫자, -,_,'.'을 제외한 모든 문자 제거
    for char in new_id:
        if char in '~!@#$%^&*()=+[{]}:?,<>/':
            new_id = new_id.replace(char,"")
    # print("step2 new_id: {}".format(new_id))
    #3. new_id에서 마침표 2번 이상 연속된 부분을 하나의 마침표로. 치환
    new_id = re.sub('\.{2,}', '.', new_id)
    # print("step3 new_id: {}".format(new_id))
    #4. 마침표가 처음, 끝에 있다면 제거
    new_id = new_id.strip('.')
    # print("step4 new_id: {}".format(new_id))
    #5. new_id가 빈 문자열이라면, 'a'를 대입
    if len(new_id) == 0:
        new_id += 'a'
    # print("step5 new_id: {}".format(new_id))
    #6. 16자 이상이면 0:15말고 모두 제거
        #제거 후 마침표가 끝에 위치한다면 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id.rstrip('.')
    # print("step6 new_id: {}".format(new_id))
    #7. new_id의 길이가 2자 이하라면 new_id[-1]을 길이가 3이 될때까지 반복해서 끝에 붙임.
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]
    # print("step7 new_id: {}".format(new_id))
    
    return new_id