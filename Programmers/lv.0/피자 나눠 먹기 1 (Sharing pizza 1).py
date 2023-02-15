# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    answer = 0
    
    
    answer = n // 7
    
    if (n < 7):
        answer = answer + 1
    else:
        if( n % 7 != 0):
            answer = answer + 1
        
    return answer
