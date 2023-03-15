# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    
    print(ord(s[0]))
    
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper():
            if ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        else:
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
                
    
    return answer