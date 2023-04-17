# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    answer = ''
    alpha = "abcdefghij"
    
    for i in str(age):
        answer += alpha[int(i)]
    
    return answer