# link :: https://school.programmers.co.kr/learn/courses/30/lessons/181847

def solution(n_str):
    answer = ''
    idx = 0
    
    for i in range(len(n_str)):
        if n_str[i] != '0':
            idx = i
            break
    
    return n_str[idx:]