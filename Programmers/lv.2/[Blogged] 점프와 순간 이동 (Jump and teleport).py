# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12980

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-2-jump-and-teleport-3d37e0f5fb4

def solution(n):
    answer = 0
    
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            answer += 1

    return answer