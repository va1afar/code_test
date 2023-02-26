# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    tmp_list = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) != 0:
        answer.sort()
    else:
        answer.append(-1)
    
    return answer
