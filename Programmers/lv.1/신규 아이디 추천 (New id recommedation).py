# link :: https://school.programmers.co.kr/learn/courses/30/lessons/72410

# 2021 KAKAO BLIND RECRUITMENT code test problem.

def solution(new_id):
    answer = ''
    allowed_list = ['-', '_', '.']
    
    for i in range(len(new_id)): 
        if new_id[i].isupper(): # Condition 1
            answer += new_id[i].lower()
        elif new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in allowed_list: # Condition 2
            answer += new_id[i]
        if new_id[i] == '.' and answer[-2:] == '..': # Condition 3
            answer = answer[:-1]
    if len(answer) >= 1 and answer[0] == '.': # Condition 4 (1)
        answer = answer[1:]
    if len(answer) >= 1 and answer[-1] == '.':# Condition 4 (2)
        answer = answer[:-1]
    if answer == '': # Condition 5
        answer = 'a'
    if len(answer) >= 16: # Condition 6 (1)
        answer = answer[0:15]
    if answer[-1] == '.': # Condition 6 (2)
        answer = answer[:-1]
    while len(answer) <= 2: # Condition 7
        answer += answer[-1]
    
    return answer