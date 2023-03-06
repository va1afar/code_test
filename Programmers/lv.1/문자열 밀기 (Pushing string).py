# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    answer = 0
    tmp_str = A
    
    if tmp_str == B:
        answer = 0
    else:
        for i in range(len(A)):
            tmp_str = tmp_str[-1] + tmp_str[0:-1]
            if tmp_str == B:
                answer = i+1
                break
            else:
                answer = -1
    
    return answer
