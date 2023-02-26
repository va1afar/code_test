# link :: https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    
    for num, i in enumerate(absolutes):
        if signs[num] == True:
            answer += i
        else:
            answer -= i
    
    return answer
