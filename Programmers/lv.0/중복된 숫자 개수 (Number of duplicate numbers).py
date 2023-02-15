# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120583

def solution(array, n):
    answer = 0
    
    for i in range(len(array)):
        if array[i] == n:
            answer += 1
    
    return answer
