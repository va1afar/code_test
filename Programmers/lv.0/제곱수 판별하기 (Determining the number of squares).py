# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120909

import math

def solution(n):
    # variable.
    answer = 0
    
    # calculation.
    n = math.sqrt(n)
    if n % 1.0 == 0.0:
        answer = 1
    else:
        answer = 2
    
    
    return answer
