# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    answer = ''

    for i in range(len(my_string)):
        answer += (my_string[i])*n
    
    return answer
