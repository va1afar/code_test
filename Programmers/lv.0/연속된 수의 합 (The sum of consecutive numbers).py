# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    # variable.
    answer = []
    bottom_num = 0
    top_num = 0
    
    # calculation.
    if num % 2 != 0:
        bottom_num = (total//num) - (num//2)
        top_num = (total//num) + (num//2)
        answer = list(range(bottom_num, top_num+1))
    else:
        bottom_num = (total//(num//2))//2 - (num-2) // 2
        top_num = (total//(num//2))//2 +1 + (num-2) // 2
        answer = list(range(bottom_num, top_num+1))
    
    return answer
