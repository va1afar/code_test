# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n):
    answer = 0
    
    if math.sqrt(n) % 1 == 0:
        answer = (math.sqrt(n)+1) ** 2
    else:
        answer = -1
    
    return answer
