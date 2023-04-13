# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120862

from itertools import combinations

def solution(numbers):
    answer = 0
    
    num_list = list(combinations(numbers, 2))
    answer = max(num[0]* num[1] for num in num_list)
    
    return answer