# link :: https://school.programmers.co.kr/learn/courses/30/lessons/181878

def solution(myString, pat):
    answer = -1
    
    myString = myString.lower()
    pat = pat.lower()
    
    if pat in myString:
        answer = 1
    else:
        answer = 0
    
    return answer