# link :: https://school.programmers.co.kr/learn/courses/30/lessons/181930

def solution(a, b, c):
    answer = 0
    
    if a != b and b != c and a != c: # if all nums diff
        answer = a + b + c
    elif a == b and b == c and a == c: # if all nums same
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    else: # if two nums are same, only one diff.
        answer = (a + b + c) * (a**2 + b**2 + c**2) 
    
    return answer