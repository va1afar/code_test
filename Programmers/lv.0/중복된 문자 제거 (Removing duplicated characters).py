# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    answer = ''
    exists = []
    
    for i in my_string:
        if i in exists:
            continue
        else:
            answer += i
            exists.append(i)
    
    return answer