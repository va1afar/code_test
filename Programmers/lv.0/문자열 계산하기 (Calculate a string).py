# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120902#

def solution(my_string):
    answer = 0
    
    strings = my_string.split()
    for i in range(len(strings)):
        if i == 0:
            answer += int(strings[i])
        elif i % 2 == 0:
            if strings[i-1] == "+":
                answer += int(strings[i])
            else:
                answer -= int(strings[i])
            
    return answer