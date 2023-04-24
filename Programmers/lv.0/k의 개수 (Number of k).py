# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    answer = 0
    
    for num in range(i, j+1):
        for n in str(num):
            if int(n) == k:
                answer += 1
    
    return answer