# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120812


from collections import Counter

def solution(array):
    answer = 0
    
    cnt = Counter(array)
    order = cnt.most_common()
    
    if len(order) >= 2:
        if order[0][1] == order[1][1]:
            answer = -1
        else:
            answer = order[0][0]
    else:
        answer = order[0][0]
    
    
    return answer
