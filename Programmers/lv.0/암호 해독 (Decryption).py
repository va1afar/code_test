# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    answer = ''
    
    for i in range(len(cipher)):
        if i % code == code-1:
            answer += cipher[i]
    
    return answer