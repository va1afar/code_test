# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
    answer = []
    
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    
    return answer