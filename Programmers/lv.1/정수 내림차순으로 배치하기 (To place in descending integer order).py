# link :: https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    answer = 0
    arr_n = []
    str_answer = ''
    
    arr_n = list(map(int,str(n))) 
    arr_n.sort(reverse=True)
    str_answer = ''.join(map(str,arr_n))
    answer = int(str_answer)
    
    return answer
