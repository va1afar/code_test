# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    
    return answer
