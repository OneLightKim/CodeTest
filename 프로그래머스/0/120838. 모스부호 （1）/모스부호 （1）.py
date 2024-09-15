def solution(letter):
    # answer = ''
    # letter =letter.split(" ")
    # for i in letter:
    #     if i in morse:
    #          answer += morse[i]
    # return answer
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    answer = ''
    for i in letter.split():
        answer += morse[i]
    return answer