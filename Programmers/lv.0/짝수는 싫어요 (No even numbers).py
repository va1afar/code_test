# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    answer = []
    number = 1
    
    while number <= n:
        answer.append(number)
        number += 2
   
    return answer
