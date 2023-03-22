# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12977

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-making-prime-numbers-85c01cbf5f16

import math
from itertools import combinations

def solution(nums):
    answer = 0
    
    for i in combinations(nums, 3):
        sqrt_i = int( math.sqrt(sum(i)) )
        for j in range(2, sqrt_i+1):
            if sum(i) % j == 0:
                break
            if j == sqrt_i:
                answer += 1
    
    return answer