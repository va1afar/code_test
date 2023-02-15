# link :: https://school.programmers.co.kr/learn/courses/30/lessons/135808

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-a-fruit-seller-baf3f367591c

def solution(k, m, score):
    # variable.
    answer = 0
    i = 0

    # calc.
    score.sort()
    i = len(score) % m
    del score[0:i]
    score = score[::m]
    answer = sum(score) * m
    
    return answer
