# link :: https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for i in goal:
        if len(cards1) > 0 and i == cards1[0]:
            del cards1[0]
        elif len(cards2) > 0 and i == cards2[0]:
            del cards2[0]
        else:
            answer = 'No'
    
    return answer