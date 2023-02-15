# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    answer = 0
    i = 1
    
    while i <= n:
        if n % i == 0:
            answer += 1
        i += 1
    
    return answer
