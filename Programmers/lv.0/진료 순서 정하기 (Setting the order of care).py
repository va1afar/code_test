# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    answer = []
    prior_emergency = sorted(emergency, reverse=True)
    
    for num in emergency:
        answer.append(prior_emergency.index(num)+1)
        
    return answer