# link :: https://school.programmers.co.kr/learn/courses/30/lessons/132267

# blogged link :: https://medium.com/@va1afar.biz/programmers-coding-test-lv-1-cola-problem-dbfb3470ce98

def solution(a, b, n):
    #valuable.
    answer = 0
    
    current_bottle = 0
    temp_bottle = 0
    total_received_bottle = 0
    
    
    #calc.
    current_bottle = n
    
    while (current_bottle >= a):
        total_received_bottle += ((current_bottle // a) * b)
        temp_bottle = current_bottle % a
        current_bottle = ((current_bottle // a) * b)+ temp_bottle
        
    answer = total_received_bottle
    
    return answer
