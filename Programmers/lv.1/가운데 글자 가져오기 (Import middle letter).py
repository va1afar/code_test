# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        answer = s[len(s)//2-1:len(s)//2+1]
    else:
        answer = s[len(s)//2:len(s)//2+1]
    
    return answer
