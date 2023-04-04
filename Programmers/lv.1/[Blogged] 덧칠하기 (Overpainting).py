# link :: https://school.programmers.co.kr/learn/courses/30/lessons/161989

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-overpainting-dccb43ccd26f

def solution(n, m, section):
    answer = 0
    next_point = 0
    
    for i in section:
        if next_point <= i:
            next_point = i+m
            answer += 1
        
    return answer