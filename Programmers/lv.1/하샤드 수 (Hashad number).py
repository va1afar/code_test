# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    str_x = str(x)
    sum_x = 0
    
    for i in range(len(str_x)):
        sum_x += int(str_x[i])
    if x % sum_x == 0:
        answer = True
    else:
        answer = False
    
    return answer
