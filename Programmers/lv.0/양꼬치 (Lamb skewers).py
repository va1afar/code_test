# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    answer = 0
    k = k - (n//10)
    
    answer = 12000*n
    answer += 2000*k
    
    return answer
