# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120846

import math

def solution(n):
    answer = 0
    
    for i in range(4, n+1): # １〜３は該当しないので。
        sqrt_i = int(math.sqrt(i))
        for j in range(2, sqrt_i+1):
            if i % j == 0:
                answer += 1
                break
    
    return answer