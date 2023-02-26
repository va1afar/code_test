# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    list_num = []
    
    if a == b :
        answer = a
    else :
        if a < b :
            answer = sum(range(a,b+1))
        else :
            answer = sum(range(b,a+1))
            
    return answer
