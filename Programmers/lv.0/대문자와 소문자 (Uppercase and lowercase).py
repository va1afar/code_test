# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    
    return answer