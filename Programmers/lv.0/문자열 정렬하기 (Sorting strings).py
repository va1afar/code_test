# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    answer = []
    
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    
    return answer