# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    answer = 0
    tmp = 1
    
    for i in range(1, 12):
        tmp *= i
        if tmp > n :
            answer = i-1
            break
    
    return answer