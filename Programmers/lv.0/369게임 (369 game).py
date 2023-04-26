# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = 0
    clap_list = ['3', '6', '9']
    
    for ch in str(order):
        if ch in clap_list:
            answer += 1
    
    return answer