# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    answer = 0
    
    for i in my_string:
        if i.isdigit():
            answer += int(i)
    
    return answer