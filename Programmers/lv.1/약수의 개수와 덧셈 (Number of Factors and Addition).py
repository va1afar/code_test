# link :: https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    
    while left <= right:
        cnt = 0
        for i in range(left):
            if left % (i+1) == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += left
        else: 
            answer -= left
        left += 1
    
    return answer
