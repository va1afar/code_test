# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    cnt = True
    
    s = s.lower()
    for i in s:
        if i.isalpha() and cnt:
            answer += i.upper()
            cnt = False
        elif i == ' ':
            answer += i
            cnt = True
        else:
            answer += i
            cnt = False
    
    return answer