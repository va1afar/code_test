# link :: https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0, 0]
    cnt_1 = 0
    
    while s != '1':
        for i in s:
            if i == '0':
                answer[1] += 1
            else:
                cnt_1 += 1
        s = format(cnt_1,'b')
        cnt_1 = 0
        answer[0] += 1
        
    return answer