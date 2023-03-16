# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    
    d.sort()
    for i in range(len(d)):
        # ifの条件を満たす時のみ引き算し、その順番をanswerに代入します。
        if budget - d[i] >= 0:
            budget -= d[i]
            answer = i + 1
    
    return answer