# link :: https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    each_list = []
    num_of_lists = len(t)-len(p)+1
    
    for i in range(num_of_lists):
        each_list.append(t[i:i+len(p)])
    for n in each_list:
        if n <= p :
            answer += 1
    
    return answer
