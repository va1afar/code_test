# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = False
    cnt = 0
    
    
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            cnt += 1
        elif s[i] == 'y' or s[i] == 'Y':
            cnt -= 1
    if cnt == 0:
        answer = True
    else:
        answer = False
    
    return answer
