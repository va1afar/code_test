# link :: https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    answer = []
    
    answer.append(max(array))
    answer.append(array.index(max(array)))
    
    return answer