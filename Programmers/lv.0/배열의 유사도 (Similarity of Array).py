# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    answer = 0
    
    for i_s1 in s1:
        for i_s2 in s2:
            if i_s1 == i_s2:
                answer += 1
    
    return answer
