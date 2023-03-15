# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120908

def solution(str1, str2):
    answer = 0
    
    if str2 in str1:
        answer = 1
    else:
        answer = 2
    
    return answer