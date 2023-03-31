# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120815

def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if (i * 6) % n == 0:
            answer = i
            break
    
    return answer