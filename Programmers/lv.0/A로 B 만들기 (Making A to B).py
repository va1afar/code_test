# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120886

def solution(before, after):
    answer = 1
    list_after = list(after)
    
    for ch in before:
        if ch in list_after:
            list_after.remove(ch)
        else:
            return 0
    
    return answer