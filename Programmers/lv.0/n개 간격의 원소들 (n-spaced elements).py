# link :: https://school.programmers.co.kr/learn/courses/30/lessons/181888

def solution(num_list, n):
    answer = []
    
    for num in num_list[::n]:
        answer.append(num)
    
    return answer