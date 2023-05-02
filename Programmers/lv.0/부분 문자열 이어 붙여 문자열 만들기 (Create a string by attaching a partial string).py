# link :: https://school.programmers.co.kr/learn/courses/30/lessons/181911

def solution(my_strings, parts):
    answer = ''
    
    for string, part in zip(my_strings, parts):
        answer += string[part[0]:part[1]+1]
    
    return answer